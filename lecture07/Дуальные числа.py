class Dual():

    result = []
    def __init__(self):
        self.Number1 = str.lower(input('Введите первое дуальное число:',))
        self.Number2 = str.lower(input('Введите второе дуальное число:',))
        self.Number1 = self.Number1.replace('e', '')
        self.Number2 = self.Number2.replace('e', '')
        n = 0
        if self.Number1[0] == '-':
            self.MinusReal.append('1')
            n = 1
        if self.Number2[0] == '-':
            self.MinusReal.append('2')
            n = 1
        for i in range(1,len(self.Number1)):
            if self.Number1[i] != '+' or '-':
                continue
            elif self.Number1[i] == '+':
                Numeric = self.Number1.split('+')
                self.ListReal.append(Numeric[0])
                self.ListImag.append(Numeric[1])
            else:
                Numeric = self.Number1.split('-')
                self.ListReal.append(Numeric[0])
                self.ListImag.append(Numeric[1])
                self.MinusImag.append('1')
                

        for i in range(1,len(self.Number2)):
            if self.Number2[i] != '+' or '-':
                continue
            elif self.Number2[i] == '+':
                Numeric = self.Number2.split('+')
                self.ListReal.append(Numeric[0])
                self.ListImag.append(Numeric[1])
            else:
                Numeric = self.Number2.split('-')
                self.ListReal.append(Numeric[0])
                self.ListImag.append(Numeric[1])
                self.MinusImag.append('2')
        if n == 1:
            for i in MinusReal:
                self.ListReal[i - 1] = '-' + self.ListReal[i - 1]
            for i in MinusImag:
                self.ListImag[i - 1] = '-' + self.ListImag[i - 1]
    
    def add(self, ListReal, ListImag):
        SumReal = int(self.ListReal[0]) + int(self.ListReal[1])
        SumImag = int(self.ListImag[0]) + int(self.ListImag[1])
        self.Sum = SumReal + SumImag
        
    def multiplication(self):
        None

print('Дуальные числа необходимо вводить таким образом:\na+Eb\n')

result1 = Dual();
print(result1.ListReal)

