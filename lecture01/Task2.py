#Задание переменных
tempC=input("Введите температуру в градусах Цельсия: ")
#Программа
try:
    tempC=float(tempC)
    tempF=1.8*tempC+32
    print("Температура в градусах Фаренгейта: ", tempF,"F")
except:
    print("Ошибка! Введите правильное значение температуры.")
input()

