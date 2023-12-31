start,end,step=input('Enter start end step values : ').split()
for n in range(int(start),int(end),int(step)):
    print(f'{n:>5}{n**2:>7}{n**3:>8}')
print()

for n in range(int(start),int(end),int(step)):
    print('{0:<5}{1:<7}{2:<8}'.format(n,n**2,n**3))