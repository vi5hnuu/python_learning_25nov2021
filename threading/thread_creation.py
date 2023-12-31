import threading
def func1():
    print('vishnu')
def func2():
    print('kumar')
th1=threading.Thread(name='my frist thread',target=func1)
th2=threading.Thread(target=func2)
th1.start()
th2.start()