#from 1 to 30

for x in range(1,31):
    a=x*x
    for y in range(x+1, 31):
        b=y*y
        for z in range(y+1, 31):
            c=z*z
            if(a+b==c):
                print(x,y,z)
            else :
                pass
