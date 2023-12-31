def move(n,sp,ap,ep):
    if n==1:
        print('move from',sp,'to',ep)
    else:
        move(n-1,sp,ep,ap)
        move(1, sp,'', ep)
        move(n - 1, ap, sp, ep)

move(3,'A','B','C')
'''
def move(3,sp,ap,ep):
    if n==1:
        print('move from',sp,'to',ep)
    else:
        move(3-1,sp,ep,ap)
        move(1, sp,'', ep)
        move(3 - 1, ap, sp, ep)
        |||||up
        def move(2,sp,ap,ep):
    if n==1:
        print('move from',sp,'to',ep)
    else:
        move(2-1,sp,ep,ap)//move from A to B go down now
        move(1, sp,'', ep)//move from A to C go down now
        move(2 - 1, ap, sp, ep)//move from B to C go down now
        ||||up
        def move(1,sp,ap,ep):
    if n==1:
        print('move from',sp,'to',ep)
    else:
       
'''