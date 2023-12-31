def my_decorator(func):
    def wrapper():
        print("=========")
        func()
        print("=========")
    return wrapper

def display():
    print("hey there")

def show():
    print("me here")

display=my_decorator(display)
display();
show=my_decorator(show)
show()