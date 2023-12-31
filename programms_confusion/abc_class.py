from abc import ABC,abstractmethod
# class printer():
class printer(ABC):
    def __init__(self,n):
        self.__name=n
    @abstractmethod
    def printt(self,docname):
        pass
class laser(printer):
    def __init__(self,n):
        super().__init__(n)

    def printt(self,docname):
        print(">>laser.print")
        print("printing",docname)


class ink(printer):
    def __init__(self, n):
        super().__init__(n)

    def printt(self, docname):
        print(">>ink.print")
        print("printing", docname)

p=laser('lase:l')
p.printt('hello.pdf')
q=ink('ink:i')
q.printt('hell2.pdf')