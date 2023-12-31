class A:
    def __init__(self):
        print("In class A")
    def a(self):
        print('function a in class A')

class B:
    def __init__(self):
        print("In class B")

    def b(self):
        print('function b in class B')

obja=A()
objb=B()

obja.a()
objb.b()


