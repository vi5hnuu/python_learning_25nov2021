import time
import threading

def square(nos):
    print('calculating suares :')
    for n in nos:
        time.sleep(0)
        print('n= ',n,'square=',n*n)

def cubes(nos):
    print('calculating cubes :')
    for n in nos:
        time.sleep(0)
        print('n= ',n,'cubes=',n*n*n)

arr=[1,3,5,7,9,11]
startTime=time.time()
th1=threading.Thread(target=square,args=(arr,))
th2=threading.Thread(target=cubes,args=(arr,))
th1.start()
th2.start()
th1.join()
th2.join()
endTime=time.time()
print('Time required=',endTime-startTime,'sec')
