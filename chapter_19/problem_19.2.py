class Date:
    def __init__(self,d,m,y):
        self.__day,self.__mth,self.__yr=d,m,y

    def __eq__(self,otherr):
        if self.__day==otherr.__day and self.__mth==otherr.__mth and self.__yr==otherr.__yr:
            return  True
        else:
            return False

d1=Date(17,11,98)
d2=Date(17,11,98)
d3=Date(17,11,19)
print(id(d1))
print(id(d2))
print(id(d3))
print(d1==d2)
print(d1==d3)