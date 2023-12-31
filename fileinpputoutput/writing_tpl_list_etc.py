s=[1,2,3,4,5,6,7,8,9,10]
t=(1,2,3,4,5,6,7,8,9,10)
u={1,2,3,4,5,6,7,8,9,10}
f=open('container','w')
f.writelines(str(s)+str('\n'))
f.write(str(t)+str('\n'))
f.write(str(u)+str('\n'))
f.close()
g=open('container','r')
# print(g.read())

# for x in g.readline():
#     print(x,end=' ')
# print()
# for x in g.readline():
#     print(x, end=' ')
# print()
# for x in g.readline():
#     print(x, end=' ')


# print(g.readline())
# print(g.readline())
# print(g.readline())

# print(g.read(31))
# print(g.read(32))
# print(g.read(32))

print(g.readlines())