import sys
lst=[i*i for i in range(10)]
gen=(i*i for i in range(10))
print(lst)
print(gen)
print(sys.getsizeof(lst))
print(sys.getsizeof(gen))