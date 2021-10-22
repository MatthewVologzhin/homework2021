import itertools as it

# Проверка числа на соблдюение условий
while True:
    try:
        NumbList = input('Введите строку типа "NdM NdM":')
        Z = NumbList.count('d')
        NumbList = NumbList.split()
        NumbList2 = []
        for h in range(len(NumbList)):
            NumbList2 += NumbList[h].split('d')
        print(NumbList2)
        for i in range(len(NumbList2)):
            if int(NumbList2[i]) == 0:
                raise ValueError
        break
    except ValueError or IndexError or ZeroDi:
        print('Вы ввели некорректное число! Попробуйте ещё раз:')

# Функция
def def1(N,M):

# Количество вариантов событий
    N = int(N)
    M = int(M)
    Variations = M**N
    print("Всего вариантов выпадения:", Variations)


# Список чисел, которые могут участвовать в перестановке
    Value = []
    for a in range(1,M+1):
        for b in range(1, N+1):
            Value.append(a)

# Список ВСЕХ перестановок
    X = list(it.permutations(Value, N))

# Отбор НУЖНЫХ перестановок по условию
    TF = 1
    while TF:
        try:
            for c in range(len(X)):
                if X.count(X[c])>1:
                    X.remove(X[c])
                elif len(X)== Variations:
                    TF = False
                else:
                    continue
        except IndexError:
            continue

# Список сумм каждой перестановки
    Score = []
    for d in range(len(X)):
        Score.append(sum(X[d]))

# Score2 - Количество повторений числа
# Вычисление вероятностей
    Score2 = []
    Chance = []
    for e in range(N, N*M+1):
        Score2.append(Score.count(e))
        print (e, '=', 100*Score2[e-N]/Variations, '%')
        Chance.append(Score2[e-N]/Variations)
        for g in (Score, Score2, Value, N, M, Variations, X):
            del g
    return print('Сумма вероятностей:', 100*sum(Chance), '%')

# Вся оставшаяся программа без функции :D
for f in range(0,len(NumbList2),2):
    def1(NumbList2[f], NumbList2[f+1])



input()
exit()
