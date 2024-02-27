import telebot
from datetime import datetime
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot('6684014130:AAG_QjSNaHdT_CfFZRu_sQ4-mJNrJfI0w6M')


@bot.message_handler(commands=['start'])
def start(message):
    
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    #button1 = KeyboardButton('view_note') не использованный функционал 
    #button2 = KeyboardButton('create_note') не использованный функционал
    button3 = KeyboardButton('/help')
    button4 = KeyboardButton('/code')
    #markup.row(button1,button2) не использованный функционал
    markup.row(button3,button4)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}', reply_markup=markup)

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 
    '''Привет, я являюсь ботом написанным студентом Шереметьев Т.А. я умею отвечать на команды: 
    
add_task - создаёт заметку по конкретной дате

list_tasks дата - показывает заметки по конкретной дате

code - даёт ссылку на открытый код''')
    

@bot.message_handler(commands=['code'])   
def site(message):    
    bot.send_message(message.chat.id,'https://github.com/Tihon56')


tasks = {}

@bot.message_handler(commands=['add_task'])
def add_task(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, "Введите дату и задачу в формате 'дата:задача'")
    bot.register_next_step_handler(msg, save_task)

def save_task(message):
    chat_id = message.chat.id
    data = message.text.split(':')
    date = data[0]
    task = data[1]
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = [task]
    bot.send_message(chat_id, "Задача успешно добавлена")


@bot.message_handler(commands=['list_tasks'])
def list_tasks(message):
    chat_id = message.chat.id
    date = message.text.split()[1]
    if date in tasks:
        task_list = tasks[date]
        bot.send_message(chat_id, f"Список задач на {date}: {', '.join(task_list)}")
    else:
        bot.send_message(chat_id, f"Задач на {date} нет")



bot.infinity_polling()