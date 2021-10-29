Text = input('Введите текст для подсчёта букв:')
a = 0
b = 0
for i in range (len(Text)):
    if Text[i].isupper():
        a += 1
    elif Text[i].islower():
        b += 1
print('Lower case:', b)
print('Upper case:', a)
        
