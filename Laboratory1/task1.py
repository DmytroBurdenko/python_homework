import math
import re


def vartypecheck():
    global Side1, Side2
    Side1 = input("Enter length of 1st side: ")
    Side2 = input("Enter length of 2nd side: ")
    while not bool(re.match("([0-9]*[.])?[0-9]+", Side1)) or not bool(re.match("([0-9]*[.])?[0-9]+", Side2)):
        print("Input is incorrect, try again!")
        vartypecheck()
    Side1 = float(Side1)
    Side2 = float(Side2)
    if Side1 == 0 or Side2 == 0:
        print("Side of triangle can't equal = 0!")
        vartypecheck()
    return Side1, Side2


print("Бурденко Дмитро Сергійович \n Лабораторна робота №1 \n Варіант 3 \n " 
      "Завдання №1. Розрахунок гіпотенузи, площі та периметра трикутника. ")
vartypecheck()
hypot = math.sqrt(Side1**2 + Side2**2)
round(hypot)
perimeter = (Side1+Side2+hypot)
area = (Side1*Side2/2)
print("Hypotenuse of triangle: ", hypot, "; \n",
      "Perimeter of triangle: ", perimeter, "; \n",
      "Area of triangle: ", area, ".")
