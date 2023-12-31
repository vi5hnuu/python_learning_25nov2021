def avgadj(lst):
    for i in range(0,len(lst)+1):
        yield(lst[i],lst[i+1])/2

lst=[10,20,30,40,50,60,70]
for i in avgadj(lst):
    print(i)