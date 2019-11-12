import re


def vartypecheck():
    global x
    x = input("Enter any value for x: ")
    while not bool(re.match("[-+]*([0-9]*[.])?[0-9]+", x)):
        print("Input is incorrect, try again!")
        vartypecheck()
    x = float(x)
    return x


print("Бурденко Дмитро Сергійович \n Лабораторна робота №1 \n Варіант 3 \n " 
      "Завдання №3. Обчислення конкретної  кусочної функції, в залежності від введеного значення х ")
vartypecheck()
if x <= -3:
    print("Функція = 9")
else:
    function = 1/(x**2 + 1)
    print("Функція = ", function)
