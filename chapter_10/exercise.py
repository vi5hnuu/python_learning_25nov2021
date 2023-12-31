'''s={1,2,3,7,6,4}
s.discard(10)
#s.remove(10) #error as 10 in not in set
print(s)

s1={10,20,30,40,50}
s2={10,20,30,40,50}
print(id(s1),id(s2))
s3={*s1,*s2}
print(s3)

s=set('kanlabs')
t=s[::-1] #sets cannot be sliced
print(t)

num={10,20,{30,40},50} # unhashable type: 'set'
print(num)

s={'tiger','lion','jackal'}
del(s)
print(s)

fruits={'kiwi','jack fruit','lichi'}
fruits.clear()
print(fruits)

s={10,25,4,12,3,8}
sorted(s)
print(s) '''

s={}
t={1,4,5,2,3}
print((s))
print(type(s),type(t),sep="___")
