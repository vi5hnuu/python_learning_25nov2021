def decorator(func):
    def wrapper():
        print('**************')
        func()
        print('~~~~~~~~~~~~~~')
    return wrapper

def display():
    print('I stand decorator')

def show():
    print('nothing grat ! me too')

d=decorator(display)
d()
s=decorator(show)
s()