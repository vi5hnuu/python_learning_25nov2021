class Number:
    def set_number(self,n):
        self.__num=n
    def get_number(self):
        return self.__num
    def print_number(self):
        print(self.__num)
    def isnegative(self):
        if self.__num<0:
            return True
        else:
            return False
    def isdivisibleby(self,n):
        if n==0:
            return False
        if self.__num%n==0:
            return True
        else:
            return False
    def absolute_value(self):
        if self.__num>=0:
            return self.__num
        else :
            return -1*self.__num

x=Number()
x.set_number(-1234)
x.print_number()
if x.isdivisibleby(5)==True:
    print('5 divides ',x.get_number())
else :
    print('5 does no divide ',x.get_number())
print('absolute value of ',x.get_number(),' is ',x.absolute_value())

