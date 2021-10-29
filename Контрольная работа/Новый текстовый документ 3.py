Text = input('Введите два слова для того, чтобы узнать, какие встречаются в обоих словах:')
try:
    Text.lower()
    Symbols = Text.split()
    if not len(Symbols) == 2:
        1/0
    Output = []
    for i in range(len(Symbols[0])):
        if Symbols[0][i] in Symbols[1] and Symbols[0][i] not in Output:
            Output.append(Symbols[0][i])
        else:
            continue
    Output.sort()
    print(','.join(Output))
except ZeroDivisionError:
    print('Вы сделали что-то не так!')

input()
exit()

