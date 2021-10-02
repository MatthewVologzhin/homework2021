#Добавленные модули
import math as m

#Задание переменных
print("Введите длину стороны A:")
a=input()

print("Введите длину стороны B:")
b=input()

print("Введите угол между A и B:")
angle=input()

#Программа
if str.isdigit(a) and str.isdigit(b) and str.isdigit(angle):

    a=int(a)
    b=int(b)
    angle=int(angle)
    c=m.sqrt(a**2+b**2-2*a*b*m.cos(m.radians(angle)))
    print("Длина третьей стороны:",c)

else:
    print("Ошибка! Введите правильные числа.")
        
