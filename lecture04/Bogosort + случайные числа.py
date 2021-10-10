# Добавление модуля "Рандом" как r

import random as r

#Цикл, который будет продолжаться до того момента
#пока пользователь не введёт два правильных числа

while True:
    
    try:
        N = input\
        ("Введите количество случайных чисел:")
        numb = input\
        ("Введите число, до которого будут генерироваться случайные числа:")
        RandomList = []
        N = int(N)
        numb = int(numb)
        for i in range(N):
            RandomList.append(r.randint(0,numb))
    
# Если число введено неправильно, то последует

    except ValueError:
        print('\033[31m\033[04m{}'.format\
              ("Введено некорректное число, попробуйте ещё раз!"))
        
# В Idle не отображаются цвета, заданные мной выше,
# но в Jupiter всё хорошо
        
        continue
        
# Если ошибок нет, значит, будет выведено:
 
    break
print('\033[01m'.format(),"Список", N,"случайных чисел:",'\033[0m'.format())
print(RandomList)

#Сортировка Bogosort:

while True:
    
    Bogosort = RandomList.copy()
    ListX = []

# На каждую j позицию листа Bogosort будет ставиться
# случайная "x", а если "x" повторяется, то её занесёт
# в список, который дорабатывается циклом while/else, чтобы
# выбирался дальнейший "x" при повторе.
    
    for j in range(N):
        x = r.randrange(N)
        if not (x in ListX):
            Bogosort[j] = RandomList[x]
            ListX.append(x)
        else:
            while x in ListX:
                x = r.randrange(N)
            else:
                ListX.append(x)
                Bogosort[j] = RandomList[x]

# Ниже следует проверка на то, является ли последовательность
# возрастающей или нет. Если значение счётика "P" примет значение
# N-1, это будет значить, что нашлся верная случайная последовательность
    
    
    p = 0
    for k in range(1,N):
        if Bogosort[k-1] <= Bogosort[k]:
            p = p + 1
            continue
        else:
            break
    if p == N - 1:
        break
    else:
        continue
        
# Попытался аналогично оформить текст, но теперь и в 
# Jupiter'е возникает при отображении неправильный текст.
# Как будет отображаться у других, не знаю.
        
print('\033[m01'.format(),"Отсортированный по Bogosort'у список:",'\033[0m'.format())
print(Bogosort)
input()
