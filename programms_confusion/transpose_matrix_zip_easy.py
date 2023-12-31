mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# [1,2,3,4],\
# [5,6,7,8],\
# [9,10,11,12]
it=zip(*mat)
print(it)
print(list(it))
it=zip(*mat) #try removing
for x in it:
    print(x)
i=0
it=zip(*mat) #try removing
transpose=[]
for t in it:
    transpose.append(t)
print(transpose)
