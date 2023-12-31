class A:
    def __init__(self):
        print("In class A")
    def a(self):
        print('function a in class A(can be accessed anywhere in programm)')
    def _a(self):
        print('function _a in class A(can be accesed from class or its sub class)')
    def __a(self):
        print('function __a in class A(private and can be accessed in class only)')

class B:
    def __init__(self):
        print("In class B")

    def b(self):
        print('function b in class B')
    def _b(self):
        print('function _b in class B')
    def __b(self):
        print('function __b in class B')

obja=A()
objb=B()

obja.a()
obja._a()
#obja.__a()
objb.b()
objb._b()
#objb.__b()


