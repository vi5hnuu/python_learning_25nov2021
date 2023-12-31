class QueueError(Exception):
    def __init__(self,msg,front,rear):
        self.errmsg=msg+' front = '+str(front)+' rear = '+str(rear)

    def get_message(self):
        return self.errmsg

class Queue:
    def __init__(self,sz):
        self.size=sz
        self.arr=[]
        self.front=self.rear=-1

    def add_queue(self,item):
        if self.rear==self.size-1:
            raise  QueueError('queue is full.',self.front,self.rear)
        else:
            self.rear+=1
            self.arr=self.arr+[item]

            if self.front==-1:
                self.front=0

    def delete_queue(self):
        if self.front==-1:
            raise QueueError('queue is empty.',self.front,self.rear)
        else:
            data=self.arr[self.front]
            if(self.front==self.rear):
                self.front=self.rear=-1
            else:
                self.front+=1
            return data
    def printall(self):
        print(self.arr)

q=Queue(5)
try:
    q.add_queue(11)
    q.add_queue(12)
    q.add_queue(13)
    q.add_queue(14)
    q.add_queue(15)
    q.printall()
    i=q.delete_queue()
    print('item deleted ',i)
    i = q.delete_queue()
    print('item deleted ', i)
    i = q.delete_queue()
    print('item deleted ', i)
    i = q.delete_queue()
    print('item deleted ', i)
    i = q.delete_queue()
    print('item deleted ', i)
    i = q.delete_queue()
    print('item deleted ', i)
except QueueError as qe:
    print(qe.get_message())
