
def Parabola(x):
    return -(x**2)+5+4*x
def Line(x):
    return -13*abs(x)
def UnkFunk(x):
    return (x**-1)+x**2+45*x

def Extremum(func, a, b):
    y0 = func(a)
    y1 = func(a)
    lol0 = 0
    lol1 = 0
    ListMin = []
    ListMax = []
    ListXMin = []
    ListXMax = []
    if a > b:
        print('Введен некорректный порядок или набор чисел!')
        exit()
    while True:
        a = a + 10**-4
        if b >= a:
            if y0 >= func(a):
                y0 = func(a)
                if func(a-10**-3) > y0 < func(a+10**-3):
                    if round(a,2) not in ListXMin:
                        ListMin.append(round(y0,1))
                        lol0 = 1
                        ListXMin.append(round(a,1))
                    else:
                        continue
                else:
                    continue
            elif y1 <= func(a):
                y1 = func(a)
                if func(a-10**-3) < y1 > func(a+10**-3):
                    if round(a,2) not in ListXMax:
                        ListMax.append(round(y1,1))
                        lol1 = 1
                        ListXMax.append(round(a,1))
                    else:
                        continue
            else:
                continue
        else:
            break
    if len(ListMin) == 0 and len(ListMax) == 0:
        return print('Наименьшее значение:',round(y0,3)
                     ,'Наибольшее значение:', round(y1,3)
                     ,'Все минимальные значения:','None'
                     ,'Все максимальные значения:','None', sep = '\n')
    else:
        CoordMax = {}
        CoordMin = {}
        for i in range(len(ListMax)):
            CoordMax.update({ListXMax[i]: ListMax[i]})
        for j in range(len(ListMin)):
            CoordMin.update({ListXMin[j]: ListMin[j]})
        return print('Наименьшее значение:',round(y0,3)
                     ,'Наибольшее значение:', round(y1,3)
                     ,'Все максимальные экстремумы:', CoordMax
                     ,'Все минимальные экстремумы:',CoordMin, 'где {x:y}',sep = '\n')


    
    
     



    


                
        
