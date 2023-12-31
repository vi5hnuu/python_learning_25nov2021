integers=[10,20,30,40,50]
floats=(1.1,2.2,3.3,4.4,5.5)
ti=zip(integers,floats)
lst=list(ti)
for i,f in lst:
    print(i,f)