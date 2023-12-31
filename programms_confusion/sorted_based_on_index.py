import operator
s="vishnuss kumarrs"
print(sorted(s))
z=''.join(sorted(set(s),key=s.index))
m=list(sorted(set(s),key=s.index))
n=list(sorted(set(s),key=operator.itemgetter(0)))
print(n)
print(tuple(sorted(set(s),key=s.index)))