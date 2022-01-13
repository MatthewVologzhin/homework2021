class Spline():
    def __init__(self, HMN):
        self.Coord = []
        print('Введите координаты вида "x, y":')
        for i in range(HMN):
            a = input(f'{i+1}. ')
            try:
                self.check(a)
            except ZeroDivisionError or ValueError:
                self.Coord = []
                print('Что-то не так с координатами!')
            a = a.split(',')
            self.Coord.append(a)
            self.Coord.sort(key = lambda x: float(x[0]))

    def check(self, a):
        for i in range(len(self.Coord)):
            if a in self.Coord[i]:
                1/0
        b = a.split(',')
        if len(b) != 2:
            1/0
        for k in range(len(b)):
            try:
                float(b[k])
            except ValueError:
                print('Число введено неправильно!')

    def __call__(self):
        print(self.Coord1)

class LinearSpline(Spline):
    def __init__(self, HMN):
        super().__init__(HMN)
        self.coeff(HMN)

    def coeff(self, HMN):
        x = self.Coord
        self.k_list = []
        self.b_list = []
        for i in range(HMN-1):
            dx = float(x[i+1][0]) - float(x[i][0])
            dy = float(x[i+1][1]) -float(x[i][1])
            k = dy/dx
            b = float(x[i][1]) - k*float(x[i][0])
            self.k_list.append(k)
            self.b_list.append(b)

    def __call__(self, x=0):
        k_list = self.k_list
        b_list = self.b_list
        Coord = self.Coord

        #Определяем, где находится вызываемый X:
        for i in range(len(k_list)):
            if (float(Coord[i][0]) < x) and (x < float(Coord[i+1][0])):
                y = float(k_list[i])*x + float(b_list[i])
                
        for j in range(len(Coord)):
            if x == float(Coord[j][0]):
                y = Coord[j][1]

        if x > float(Coord[-1][0]):
            y = float(k_list[-1])*x + float(b_list[-1])
        elif x < float(Coord[0][0]):
            y = float(k_list[0])*x + float(b_list[0])
            
        print('y = ', y)
        
        
        
        
        
