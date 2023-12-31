l=[(10,20,30),(150.55,145.60,157.65),('A1','B1','C1')]
for a in zip(*l):
    print(a);
print()

for a in zip(*l):
    print(*a);
print()

for a,b,c in zip(*l):
    print(a,b,c);
print()

c=[]
for a in zip(*l):
    c.append(a);
print(c)