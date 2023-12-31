def headprint(n):
    if n==0:
        return
    else :
        headprint(n-1)
        print(n,end="|")

headprint(5)

''' 
def headprint(5):
    if n==0:
        return
    else :
        headprint(5-1)
        print(5)== print 5
        
        def headprint(4):
    if n==0:
        return
    else :
        headprint(4-1)
        print(4)==print 4
        
        def headprint(3):
    if n==0:
        return
    else :
        headprint(3-1)
        print(3)==print 3
        
        def headprint(2):
    if n==0:
        return
    else :
        headprint(2-1)
        print(2)==print 2
        |||||
        def headprint(1):
    if n==0:
        return
    else :
        headprint(1-1)=none
        print(1)=print 1==out of loop=go to last call
        |||||||
        def headprint(0):
    if n==0:
        return
    else :
        headprint(0-1)
        print(0)
'''