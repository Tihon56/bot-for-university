
while True:
    try:
        x = int(input("Введите число принадлежащие промежутку 100 - 999: "))
        if 100<=x<=999:
            break
        else:
            print("Число должно принадлежать промежутку 100-999") 
    except ValueError:
        print("Ошибка! Вводите число.")
    
x = str(x)
x = int(x[2]+x)
print(x)
print(type(x))