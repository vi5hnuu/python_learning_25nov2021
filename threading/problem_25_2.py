import time
import threading

def square(nos):
    print('calculating suares :')
    for n in nos:
        time.sleep(2)
        print('n= ',n,'square=',n*n)

def cubes(nos):
    print('calculating suares :')
    for n in nos:
        time.sleep(2)
        print('n= ',n,'cubes=',n*n*n)

arr=[1,3,5,7,9,11]
startTime=time.time()
square(arr)
cubes(arr)
endTime=time.time()
print('Time required=',endTime-startTime,'sec')

#compare when it runs on independents thread.......problem_25_2_latest.py