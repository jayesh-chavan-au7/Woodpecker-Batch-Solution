class complex(object):
    def __init__(self, real, img):
        self.real = float(real)
        self.imaginary = float(img)

    def __add__(self, other):
        return complex(self.real+other.real, self.imaginary+other.imaginary)

    def __sub__(self, other):
        return complex(self.real-other.real, self.imaginary-other.imaginary)

    def __mul__(self, other):
        return complex((self.real*other.real-self.imaginary*other.imaginary), (self.real*other.imaginary+self.imaginary*other.real))

    def __truediv__(self, other):
        complexConj = complex(other.real, -other.imaginary)
        numrator = complex.__mul__(self, complexConj)
        denomintor = other.real**2+other.imaginary**2
        return complex(numrator.real/denomintor, numrator.imaginary/denomintor)

    def mod(self):
        return complex(pow((self.real**2)+(self.imaginary**2), 0.5), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = '{:.2f}+0.00i'.format(self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = '0.00+{:.2f}i'.format(self.imaginary)
            elif self.imaginary < 0:
                result = '0.00-{:.2f}i'.format(abs(self.imaginary))
        elif self.imaginary > 0:
            result = '{:.2f}+{:.2f}i'.format(self.real, self.imaginary)
        else:
            result = '{:.2f}+{:.2f}i'.format(self.real, abs(self.imaginary))
        return result


x = complex(2, 1)
y = complex(5, 6)

print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
