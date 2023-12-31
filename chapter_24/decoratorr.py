def decorator(func):
    def wrapper():
        print('**************')
        func()
        print('~~~~~~~~~~~~~~')
    return wrapper
@decorator
def display():
    print('I stand decorator')
@decorator
def show():
    print('nothing grat ! me too')

display()
show()