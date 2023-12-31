names=['amon','anil','akash']
age=[25,23,27]
salaries=[35000.0,45000.0,35500.70]
it=zip(names,age,salaries)
lst=list(it)
print(lst)
n,a,s=zip(*lst)
print(n)
print(a)
print(s)

for m in lst:
    print(m[0],m[1],m[2])

