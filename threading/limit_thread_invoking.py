import threading

def fun(msg):
    s.acquire()
    t=threading.current_thread()
    while True:
        print(t.name,':',msg)
    s.release()

s=threading.BoundedSemaphore(3)
th1=threading.Thread(target=fun,args=('hello',))
th2=threading.Thread(target=fun,args=('helloo',))
th3=threading.Thread(target=fun,args=('hellooo',))
th4=threading.Thread(target=fun,args=('helloooo',))
th1.start()
th2.start()
th3.start()
th4.start()
th1.join()
th2.join()
th3.join()
th4.join()