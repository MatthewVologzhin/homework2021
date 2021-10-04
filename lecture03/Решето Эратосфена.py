try:
    n=int(input("Введите число, до которого идёт поиск простых:"))
    Numb=list(range(n))

#Этот цикл отвечает за 2ой множитель
    for j in range(2,n):

#Этот цикл отвечает за 1ый множитель
        for i in range(2,n):
            cyc1 = i
            step = 0
            cyc2 = j
            while step <= n:
                cyc1 = cyc2 * cyc1
                if cyc1 in Numb:
                    Numb[cyc1] = 0
                    step = step + 1
                else:
                    break

#Фрагмент кода, убирающий нули
    for k in range(n):
        if 0 in Numb:
            Numb.remove(0)
    Numb.remove(1)
    print("Список всех простых чисел:",Numb)
    print("Всего",len(Numb),"простых чисел содержится до",n)
except ValueError:
    print("Вы ввели некорректное значение числа.")
input()
