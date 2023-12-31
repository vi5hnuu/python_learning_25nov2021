import operator
s='razmattaz'
s=''.join(sorted(set(s),key=s.index))
print(s)

lst=['r','a','a','z','m','a','t','t','a','z']
lst=list(sorted(set(lst),key=lst.index))
print(lst)

tpl=('r','a','a','z','m','a','t','t','a','z')
tpl=tuple(sorted(set(tpl),key=tpl.index))
print(tpl)