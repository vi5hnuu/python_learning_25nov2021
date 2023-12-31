class fruit:
    count=0

    def __init__(self,name='',size=0,color=''):
        self.__name=name
        self.__size = size
        self.__color = color
        fruit.count+=1

    def display():
        print(fruit.count)
f1=fruit('banana',5,'yellow')
f2=fruit('orange',4,'orange')
fruit.display()
print(fruit.count)

