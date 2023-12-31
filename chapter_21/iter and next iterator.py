lst=[10,20,30,40,50]
for x in lst:
    print(x,end=' ')
print()
i=lst.__iter__()
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
print()
z=iter(lst)
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))


