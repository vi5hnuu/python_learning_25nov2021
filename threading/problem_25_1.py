import threading
import time
def fun1():
    t=threading.current_thread()
    print('starting',t.name)
    time.sleep(3)
    print('exiting',t.name)

def fun2():
    t=threading.current_thread()
    print('starting',t.name)
    time.sleep(3)
    print('exiting',t.name)

def fun3():
    t=threading.current_thread()
    print('starting',t.name)
    time.sleep(3)
    print('exiting',t.name)

t1=threading.Thread(target=fun1)
t2=threading.Thread(name='my second thread',target=fun2)
t3=threading.Thread(name='my third thread',target=fun3)
t1.start()
t2.start()
t3.start()