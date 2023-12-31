class fruit:
    count=0
    def __init__(self,name='',size=0,color=''):
        print("cons called.")
        self.__name=name
        self.namee='vishnu'
        self.__size=size
        self.__color=color
        fruit.count+=1
    def display():#called by class
        print(fruit.count)

f1=fruit('banana',5,'red')
f2=fruit('xyz',6,'blue')
f3=fruit()
print(fruit.count)
fruit.display()
#print(f1.__name)
print(f1.namee)