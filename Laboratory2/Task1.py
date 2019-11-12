import re


def index():
    global iMax
    iMax = input("Enter an integer value for iMax that is >= 1: ")
    if bool(re.fullmatch("[-+]*[0-9]+", iMax)):
        iMax = float(iMax)
        iMax = int(iMax)
        if iMax < 1:
            print("You entered an incorrect symbol. Try again.")
            index()
    else:
        print("Incorrect input! Try again.")
        index()
    return iMax


def typecheck():
    global x
    x = input("Enter any value for x: ")
    while not bool(re.match("[-+]*([0-9]*[.])?[0-9]+", x)):
        print("Input is incorrect, try again!")
        typecheck()
    x = float(x)
    return x


print("Бурденко Дмитро Сергійович \n Лабораторна робота №2 \n Варіант 3 \n " 
      "Завдання №1. Обчислення суми по формулі.")
ans = 0
index()
typecheck()

for i in range(1, iMax+1):
    ans = ans+(i**2-x**2)
print("Sum = ", ans)
