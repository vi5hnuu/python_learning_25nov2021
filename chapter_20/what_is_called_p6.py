class A:
    count=0
    def __init__(self):
        super().__init__()
        print("In class A")
        A.count+=1
    def a(self):
        print('function a in class A')


    def _counter():
        print(A.count,' objects created till now.')


class B(A):
    def __init__(self):
        super().__init__()
        print("In class B")

    def b(self):
        print('function b in class B')


class C(B):
    def __init__(self):
        super().__init__()
        print("In class C")
    def c(self):
        print('function c in class C')

class D(C):
    count = 0
    def __init__(self):
        super().__init__()
        print("In class D")

    def d(self):
        print('function d in class D')

objd=D()
D._counter()
D._counter()
print()
objc=C()
C._counter()
print()
objb=B()
B._counter()
print()
obja=A()
A._counter()
A._counter()



