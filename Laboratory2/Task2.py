import re


def vartypecheck():
    global num
    num = input("Enter an integer value for num that is >= 1: ")
    if bool(re.fullmatch("[-+]*[0-9]+", num)):
        num = int(num)
        if num < 1:
            print("You entered an incorrect symbol. Try again.")
            vartypecheck()
    else:
        print("Incorrect input! Try again.")
        vartypecheck()
    num = str(num)
    return num


print("Бурденко Дмитро Сергійович \n Лабораторна робота №2 \n Варіант 3 \n " 
      "Завдання №2. Знаходження кількості парних цифер у числі.")
count = 0
vartypecheck()
for digit in num:
    try:
        digit = int(digit)
    except ValueError:
        continue
    if digit % 2 == 0:
        count += 1
print("Кількість парних чисел:", count)
