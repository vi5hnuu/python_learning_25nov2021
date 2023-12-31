tpl=('F','I','a','a','b','e','r','g','a','s','s','t','e','d')
tpl=tpl+('!',)
print(tpl)
# chk these
s=''.join(tpl)
print(s)
s='_'.join(tpl)
print(s)
s=str(tpl)
print(s)

t=tpl[3:5]
print(t)

count=tpl.count('e')
print('count=',count)

print('r' in tpl)

lst=list(tpl)
print(lst)

tpl=tpl[:3]+tpl[7:]
print(tpl)