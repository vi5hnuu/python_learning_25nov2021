class QueueError(Exception):
    def __init__(self,msg,front,rear):
        self.__errmsg=msg+' front= '+str(front)+' rear= '+str(rear)

    def get_message(self):
        return self.__errmsg

class queue:
    def __init__(self,sz):
        self.__size=sz
        self.__arr=[]
        self.__front=self.__rear=-1

    def add_queue(self,item):
        if self.__rear==self.__size-1:
            raise QueueError('Queue is full',self.__front,self.__rear)
        else:
            self.__rear+=1
            self.__arr=self.__arr+[item]

            if self.__front==-1:
                self.__front=0
    def delete_queue(self):
        if self.__front==-1:
            raise QueueError('Queue is empty',self.__front,self.__rear)
        else:
            data=self.__arr[self.__front]
            if(self.__front==self.__rear):
                self.__front=self.__rear=-1
            else:
                self.__front+=1
            return data;
    def printall(self):
        print(self.__arr[self.__front:self.__rear+1])

q=queue(5)
try:
    q.add_queue(11)
    q.add_queue(12)
    q.add_queue(13)
    q.add_queue(14)
    # q.add_queue(15)
    q.add_queue(15)
    q.printall()
    i=q.delete_queue()
    print('item deleted',i)
    i=q.delete_queue()
    print('item deleted',i)
    i=q.delete_queue()
    print('item deleted',i)
    i=q.delete_queue()
    print('item deleted',i)
    i=q.delete_queue()
    print('item deleted',i)
    # i=q.delete_queue()
    # print('item deleted',i)
    q.printall()
except QueueError as qe:
    print(qe.get_message())
finally:
    print('over')