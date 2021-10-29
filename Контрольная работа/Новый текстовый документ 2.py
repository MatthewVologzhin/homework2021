Text = input('Введите слово для подсчёта количества повтора букв:')
try:
    if not len(Text) == 1:
        1/0
    Symbols = list(Text)
    Data = []
    for i in range(len(Symbols)):
        if not Symbols[i] in Data:
            Data.append(Symbols[i])
            Data.append(str(Symbols.count(Symbols[i])))
        else:
            continue
    for j in range(0,len(Data),2):
        print(Data[j], '=', Data[j+1])
    Data.sort()
    print(Data)

except ZeroDivisionError:
    print('Вы ввели больше или меньше одного числа!')
input()
exit()

