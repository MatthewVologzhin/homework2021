# Добавление модуля "Рандом" как r

import random as r

# Цикл, который будет продолжаться до того момента
# пока пользователь не введёт два правильных числа

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
            RandomList.append(r.randrange(numb+1))
    
# Если число введено неправильно, то последует

    except ValueError:
        print('\033[31m\033[04m{}'.format\
              ("Введено некорректное число, попробуйте ещё раз!"))
        
# В Idle не отображаются цвета, заданные мной выше, ->
# но в Jupiter всё хорошо
        
        continue
        
# Если ошибок нет, значит, будет выведено:
 
    break
print('\033[01m'.format(),"Список", N,"случайных чисел:",'\033[0m'.format())
print(RandomList)

# Cортировка пузырьком:

YN=input("Хотите ли вы отсортировать список? (1 - Да \ Любое другое число - Нет):")

# YN - Параметр выбора необходимости сортировки

try:
    YN = int(YN)
    if YN == 1:
        z = range(N)
        for j in z:
            for k in range(N):
                try:
                    x = RandomList[k]
                    while RandomList[k] > RandomList[k+1]:
                        RandomList.remove(RandomList[k])
                        RandomList.insert(k + 1, x)
                except IndexError:
                    break
                    z = z - 1
        print("\033[01m{}\033[0m".format("Отсортированный пузырьком список:"))
        print(RandomList)
except ValueError:
    print('\033[31m\033[04m{}'.format('Вы ввели недопустимый ответ на вопрос, поэтому он сочтён за "Нет".'))
input()
