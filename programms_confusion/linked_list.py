class node:
    def __init__(self,car,price):
        self.car=car
        self.price=price
        self.next=None

class linklist:
    def __init__(self):
        self.head=None

    def add(self,c,pr):
        n=node(c,pr)
        if self.head is None:
            self.head=n
        else:
            p=self.head;
            while p.next is not None:
                p=p.next

            p.next=n
    def display(self):
        p=self.head
        while p is not None:
            print(p.car,p.price)
            p=p.next

listt=linklist()
listt.add('bmw','55 lac')
listt.add('tesla','70 lac')
listt.display()