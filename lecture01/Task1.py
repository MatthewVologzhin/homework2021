import math as m
a=float(input("Введите длину стороны A: "))
b=float(input("Введите длину стороны B: "))
d=float(input("Введите угол между сторонами A и B: "))
e=m.cos(m.radians(float(d)))
c=m.sqrt(float(a)**2+float(b)**2-2*float(b)*float(a)*float(e))
print("Сторона C равна: ", c)
input()
