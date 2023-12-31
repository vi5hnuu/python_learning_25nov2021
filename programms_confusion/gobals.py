def fun1():
    print("inside fun1")
def fun2():
    print("inside fun2")
def fun3():
    print("inside fun3")
def fun4():
    print("inside fun4")

lst=['fun1','fun2','fun3','fun4']
# for x in lst:
#     x()

for x in lst:
    globals()[x]()