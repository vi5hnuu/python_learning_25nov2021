def my_decorator(func):
    def wrapper():
        print("=========")
        func()
        print("=========")
    return wrapper
@my_decorator
def display():
    print("hey there")
@my_decorator
def show():
    print("me here")

display()
show()
