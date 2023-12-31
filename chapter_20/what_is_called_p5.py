class A:
    count=0
    def __init__(self):
        super().__init__()
        print("In class A")
    def a(self):
        print('function a in class A')

    def counter():
        A.count+=1
        print(A.count)

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

class D(C): #counter give wrong count as inheriting add +1 every time as for class b count is already 1
    def __init__(self): # for class c count is already 1///chek program p6
        super().__init__() #multile call to counter increase obj count and that is wrong as well
        print("In class D")

    def d(self):
        print('function d in class D')

objd=D()
D.counter() #wrong
D.counter() #wrong count shold not increase
print()
objc=C()
C.counter()
print()
objb=B()
B.counter()
print()
obja=A()
A.counter()



