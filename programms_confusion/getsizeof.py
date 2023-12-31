import sys
lst=[i*i for i in range(15)]
lstt=(i*i for i in range(15))
print(lst)
print(lstt)
print(list(lstt))
print(sys.getsizeof(lst))
print(sys.getsizeof(lstt))