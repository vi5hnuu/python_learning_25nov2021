import threading

class Ex(threading.Thread):
    def __init__(self,s):
        threading.Thread.__init__(self)
        self.msg=s

    def run(self):
        while True:
            print(self.msg,end='\n')

th1=Ex('hello')
th1.start()
th2=Ex('hi')
th2.start()
