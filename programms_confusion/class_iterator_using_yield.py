def advgadj(data):
    for i in range(0,len(data)-1):
        yield (data[i]+data[i+1])/2

lst=[10,20,30,40,50,60]
for i in advgadj(lst):
    print(i)
