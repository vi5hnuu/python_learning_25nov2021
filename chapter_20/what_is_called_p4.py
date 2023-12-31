class A:
    def __init__(self):
        print("In class A")
    def a(self):
        print('function a in class A')

class B(A):
    def __init__(self):
        print("In class B")

    def b(self):
        print('function b in class B')

class C(B):
    def __init__(self):
        print("In class C")
    def c(self):
        print('function c in class C')

class D(C):
    def __init__(self):
        print("In class D")

    def d(self):
        print('function d in class D')

objd=D()
print()
objc=C()
print()
objb=B()
print()
obja=A()



