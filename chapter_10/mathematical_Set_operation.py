#sets
engineers={'vijay','sanjay','sujay','ajay','dinesh'}
managers={'aditya','sanjay'}

print(engineers|managers)
print(engineers & managers)
print(engineers-managers)
print(managers-engineers)
print(engineers^managers)
a={1,2,3,4,5}
b={2,4,5}
print(a>=b)
print(a<=b)
print(a.issuperset(b))
print(a.issubset(b))
print(a.isdisjoint(b))
a^=b
print(a)
