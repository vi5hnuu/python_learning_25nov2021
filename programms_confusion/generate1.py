def generate(n):
    t=[]
    lol=[[] for i in range(n**n)]
    helper(n,t,lol)
    return(lol)

def helper(n,t,lol):
    global j
    if(len(t)==n):
        lol[j]=lol[j]+t
        j+=1
        return
    for i in range(1,n+1):
        t.append(i)
        helper(n,t,lol)
        t.pop()
j=0;
im=generate(3)
print(im)

#working###########################
'''
//call 1 
def helper(3,t,lol):
    global j====0
    if(len(t)==3):
        lol[j]=lol[j]+t
        j+=1
        return
    for i in range(1,n+1):
        t.append(i)  --->t=[1]
        helper(3,t=[1],lol) //call2
        t.pop()
        
//call2      
def helper(3,t=[1],lol):
    global j
    if(len(t)==n):
        lol[j]=lol[j]+t
        j+=1
        return
    for i in range(1,n+1):
        t.append(i) --->t=[1,1],[1,2]
        helper(3,t=[1,1],[1,2],lol) //call 3
        t.pop()==t-->[1]
//call 3      
def helper(3,t=[1,1],lol):
    global j
    if(len(t)==n):
        lol[j]=lol[j]+t
        j+=1
        return
    for i in range(1,n+1):
        t.append(i)--->t=[1,1,1],[1,1,2],[1,1,3]
        helper(n,t,lol) //call 4-->j==1,2,3
        t.pop()-->t=[1,1] //go to call 2 line 44
//call4       
def helper(n,t,lol):
    global j
    if(len(t)==3):
        lol[j]=lol[j]+t
        j+=1
        return //go to call 3 at line 55
    for i in range(1,n+1):
        t.append(i)
        helper(n,t,lol)
        t.pop() '''

