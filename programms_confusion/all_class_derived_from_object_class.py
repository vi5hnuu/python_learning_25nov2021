print(dir(object))
print(vars(object))
#print(dir(any class name))

class a:
    def __int__(self):
        print("hey")

v=a()
print(a.__sizeof__(v))