lst=[0,1]
lstt=[lst.append(lst[k-1]+lst[k-2]) for k in range(2,20)]
print(lst)
print(lstt)