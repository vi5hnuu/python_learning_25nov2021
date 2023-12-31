import math
class complex():
    def __init__(self,x,y):
        self.real=x
        self.imag=y
    def display(self):
        print(self.real,'+',self.imag,'i')

    def add(self,x):
        r=self.real+x.real
        i=self.imag+x.imag
        return complex(r,i)

    def substract(self,x):
        r=self.real-x.real
        i=self.imag-x.imag
        return complex(r,i)

    def multiply(self,x):
        r=self.real*x.real
        i=self.imag*x.imag
        return complex(r,i)

    def conj(self):
        r=self.real
        i=-self.imag
        return complex(r,i)

    def mods(self):
        mod2=self.real*self.real+self.imag*self.imag
        return math.sqrt(mod2)

    def divide(self,x):
        m=x.mods()
        c=x.conj()
        if m==0:
            print('Unable to divide the complex numbers')
        else:
            quo=self.multiply(c)
            quo.real=quo.real/m
            quo.imag=quo.imag/m
            return quo

a=complex(2,3)
b=complex(6,-1)
print('a : ',end='')
a.display()
print('b : ',end='')
b.display()
c=a.add(b)
print('a+b=',end='')
c.display()
d=a.substract(b)
print('a-b=',end='')
d.display()
e=a.multiply(b)
print('a*b=',end='')
e.display()
f=a.divide(b)
print('a/b=',end='')
e.display()


