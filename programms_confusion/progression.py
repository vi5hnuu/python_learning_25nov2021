class progression:
    def __init__(self,start=0):
        self._cur=start
    def __iter__(self):
        return  self
    def advance(self):
        self._cur+=1

    def __next__(self):
        if self._cur==None:
            raise StopIteration
        else:
            data=self._cur
            self.advance()
            return data
    def display(self,n=10):
        print(' '.join(str(next(self)) for i in range(n)))
class AP(progression):
    def __init__(self,start=0,step=1):
        super().__init__(start)
        self.__step=step;

    def advance(self):
        self._cur+=self.__step


class GP(progression):
    def __init__(self, start=1, step=2):
        super().__init__(start)
        self.__step = step;

    def advance(self):
        self._cur *= self.__step


class FP(progression):
    def __init__(self, first=0, second=1):
        super().__init__(first)
        self.__prev =second-first;

    def advance(self):
        self.__prev,self._cur=self._cur,self.__prev+self._cur

print('Default progresion')
p=progression()
p.display(10)
print('Ap with step of 5')
a=AP(0,5)
a.display(10)
g=GP(10)
g.display(10)
h=GP()
h.display(10)
f=FP(10,6)
f.display()
