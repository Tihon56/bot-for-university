def arithmetic (first_number,second_number,operation): 
    match operation:
        case "+":
            print(f"{first_number} + {second_number} = {first_number+second_number}")
        case "-":
            print(f"{first_number} - {second_number} = {first_number-second_number}")
        case "/":
            print(f"{first_number} / {second_number} = {first_number/second_number}")
        case "*":
            print(f"{first_number} * {second_number} = {first_number*second_number}")
        case _:
            print("«Неизвестная операция»")

#Можете проверить, для этого уберите ''' ниже
            
'''
first_number = 0
second_number = 0
operation = ""

while True:
    try:
        first_number = float(input("Введите 1-ое число: "))
        second_number = float(input("Введите 2-ое число: "))
        break 
    except ValueError:
        print("Ошибка! Вводите числа.")

operation = input("Введите тип операции:")
arithmetic(first_number,second_number,operation)
'''