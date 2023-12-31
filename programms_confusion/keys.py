d={'x':100,'y':200,'z':300}
m=[1,2,3]
print(list(map(lambda x:x*x,m)))
print(max(list(map(lambda x:d[x],d.keys()))))