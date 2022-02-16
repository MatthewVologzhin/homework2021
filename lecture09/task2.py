class Number:
    def __init__(self,numb):
        self.numb = numb

    @property
    def dec(self):
        return self.numb

    @property
    def bin(self):
        return bin(self.numb)

    @property
    def hex(self):
        return hex(self.numb)

    @property
    def roman(self):
        return r.write_roman(self.numb)


n = Number(401)
n = n + Number(100)

# примеры свойств
print(n.dec)
print(n.bin)
print(n.hex)
#print(n.roman)
