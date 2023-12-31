class InsufficientBalanceError(Exception):
    def __init__(self,accno,cb):
        self.__accno=accno
        self.__curbal=cb

    def get_details(self):
        return {'acc no':self.__accno,'current balance':self.__curbal}

class customers:
    def __init__(self):
        self.__dct={}

    def append(self,accno,n,bal):
        self.__dct[accno]={'name':n,'balance':bal}

    def deposit(self,accno,amt):
        d=self.__dct[accno]
        d['balance']=d['balance']+amt
        self.__dct[accno]=d

    def display(self):
        for k,v in self.__dct.items():
            print(k,v)
        print()

    def withdraw(self,accno,amt):
        d=self.__dct[accno]
        curbal=d['balance']
        if curbal-amt<5000:
            raise InsufficientBalanceError(accno,curbal)
        else:
            d['balance']=d['balance']-amt
            self.__dct[accno]=d

c=customers()
c.append(123,'sanjay',9000)
c.append(101,'sameer',8000)
c.append(423,'ajay',7000)
c.append(133,'sanket',6000)

c.display()
c.deposit(123,1000)
c.deposit(423,2000)
c.display()

try:
    c.withdraw(423,3000)
    print('amount withdrawn successfully')
    c.display()
    c.withdraw(101,5000)
    print('aamount withdrawn successfully')
    c.display()
except InsufficientBalanceError as ibe:
    print('withddrawn denied')
    print('insuffecient balance')
    print(ibe.get_details())
    print(ibe)
    print(ibe.args)


