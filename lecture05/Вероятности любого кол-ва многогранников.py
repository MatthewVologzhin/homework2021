import itertools as it

# Проверка числа на соблдюение условий
while True:
    try:

        NumbList = input('Введите строку типа "NdM", вводя через пробел\
все необходимые строки такого типа:')
        print('')

        Z = NumbList.count('d')
        NumbList = NumbList.split()
        NumbList2 = []

        for h in range(len(NumbList)):
            NumbList2 += NumbList[h].split('d')
        for i in range(len(NumbList2)):
            if int(NumbList2[i]) == 0:
                raise ValueError
        break

    except ValueError or IndexError:
        print('Вы ввели некорректное число! Попробуйте ещё раз:')

# Функция
def Probabilities(N,M):

# Количество вариантов событий
    N = int(N)
    M = int(M)
    Variations = M**N
    print('\033[31m\033[03m{}\033[00m'.format("Всего вариантов выпадения:", Variations))


# Список чисел, которые могут участвовать в перестановке
    Value = []
    for a in range(1,M+1):
        Value.append(a)

# Список ВСЕХ перестановок
    X = list(it.product(Value, repeat = N))


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
    return print('Сумма вероятностей:', round(100*sum(Chance), 3), '%', '\n')

# Вся оставшаяся программа без функции :D
for f in range(0,2*Z,2):
    Probabilities(NumbList2[f], NumbList2[f+1])



input()
exit()
