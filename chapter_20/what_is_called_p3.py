class A:
    def __init__(self):
        print("In class A")
    def a(self):
        print('function a in class A')
    def _a(self):
        print('function _a in class A')
    def func(self):
        self._a()
    def __a(self): #prevent from overridden
        print('function __a in class A')

class B(A):
    def __init__(self):
        super().__init__()
        print("In class B")
    def a(self):
        print('function a in class B')
    def _a(self):
        print('function _a in class B')
    def __a(self):
        print('function __a in class B')
    def b(self):
        print('function b in class B')
    def _b(self):
        print('function _b in class B')
    def __b(self):
        print('function __b in class B')


    def __a(self):
        print('function __b in class B')
    def func(self):
        self.__a()

obja=B()
objb=A()

obja.a()
obja._a()
#obja.__a()
obja.b()
obja._b()
#obja.__b()

objb._a()

obja.func()
objb.func()








