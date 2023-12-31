words=['a','coddle','called','molly']
number=[10,20,30,40]

for ele in zip(words,number):
    print(ele[0],ele[1],end="/")
print()
for ele in zip(words,number):
    print(*ele,end='/')
print()
for e,le in zip(words,number):
    print(e,le,end="/")
print()

a=[(x,y) for x in words for y in number if x!=y]
print(a)

w,n=zip(*a)
print(set(w))
print(set(n))

