lst={'aditya','aditi','ankita','anuja','bhushan','bahu','bali','bhoomi','babhoti'}
t=set()
s=set()

for item in lst :
    if item.startswith('a'):
        t.add(item)
    elif item.startswith('b'):
        s.add(item)
print(s)
print(t)
