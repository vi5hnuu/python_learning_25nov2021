import operator
tpl=([1,2,3,4],[10,20])
tpl[1][0]=21
#s[2]='special' immutable
print(tpl)
print(sorted(tpl))  #list
#
p=tpl[1]
p[1]=22
print(tpl)