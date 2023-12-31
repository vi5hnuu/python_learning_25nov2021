import  threading
import random
import time

def fun(ev,n):
    for i range(n):
        print(i+1,'waiting for the flag to be set...')
        ev.wait()
        print('wait complete at :',time.ctime())
        ev.clear()
        print()
def fun1(ev,n):
    for i in range(n):
        time.sleep(random.randrange(2,5))
        ev.set()

ev=threading.Event()
th=[]
num=random.randrange(4,8)
th.append(threading.current_thread())

#incomplete