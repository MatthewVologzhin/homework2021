import itertools as it

# Проверка числа на соблдюение условий
while True:
    try:
        NumbList = input('Введите строку типа NdM:')
        NumbList = NumbList.split('d')
        if (len(NumbList) == 2
        and int(NumbList[0])
        and int(NumbList[1])):
            break
        else:
            print('Вы ввели некорректное число! Попробуйте ещё раз:')
            continue
    except ValueError:
        print('Вы ввели некорректное число! Попробуйте ещё раз:')


# N - кол-во кубиков
N = int(NumbList[0])

# M - кол-во граней
M = int(NumbList[1])    

# Количество вариантов событий
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
    print (e, '=', Score2[e-N]/Variations, '%')
    Chance.append(Score2[e-N]/Variations)    
print('Сумма вероятностей:', sum(Chance))
input()
exit()
