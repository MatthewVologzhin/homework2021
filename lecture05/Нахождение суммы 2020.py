File1 = open('task1.txt')
NumbList = [int(x) for x in File1] 

# Цикл, задающий первый член суммы
for i in range(len(NumbList)):

# Цикл, задающий второй член суммы
    for j in range(1+i,len(NumbList)):

# Цикл, задающий третий член суммы
        for k in range(2+j, len(NumbList)):

# Создаёт преднамеренную ошибку, чтобы закончить
# преждевременно цикл после нахождения такой суммы
            try:
                if (NumbList[i]
                + NumbList[j]
                + NumbList[k]) == 2020:
                    print('Числа, дающие в сумме 2020:',
                          NumbList[i],
                          NumbList[j],
                          NumbList[k])
                    multi = NumbList[i] * NumbList[j] * NumbList[k]
                    print('Произведение этих чисел:',multi)

# Та самая ошибка, о которой говорил выше
                    stop = int('error')

            except ValueError:
                File2 = open('output1.txt', 'w')
                File2.writelines(['Произведение трёх чисел из списка:',str(multi)])

# Не забываем закрывать файлы ;)
                File1.close()
                File2.close()
                input()
exit()
