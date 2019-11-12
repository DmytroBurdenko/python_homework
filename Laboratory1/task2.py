import re


def varcheck():
    global Angle1, Angle2
    Angle1 = input("Enter value of 1st angle: ")
    Angle2 = input("Enter value of 2nd angle: ")
    while not bool(re.match("([0-9]*[.])?[0-9]+", Angle1)) or not bool(re.match("([0-9]*[.])?[0-9]+", Angle2)):
        print("Input is incorrect, try again!")
        varcheck()
    Angle1 = float(Angle1)
    Angle2 = float(Angle2)
    if Angle1 == 0 or Angle2 == 0:
        print("Angle of triangle can't equal 0!")
        varcheck()
    elif Angle1 >= 180 or Angle2 >= 180:
        print("Angle of triangle can't be more than or equal to 180 degrees!")
        varcheck()
    return Angle1, Angle2


print("Бурденко Дмитро Сергійович \n Лабораторна робота №1 \n Варіант 3 \n " 
      "Завдання №2. Перевірка трикутника на прямокутність та існування за його кутами. ")
varcheck()
if (Angle1+Angle2) >= 180:
    print("Такого трикутника не існує.")
elif (Angle1+Angle2) == 90:
    print("Трикутник існує і є прямокутним.")
else: 
    print("Трикутник існує, але не є прямокутним.")
