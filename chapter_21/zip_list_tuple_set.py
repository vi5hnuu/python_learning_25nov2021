words=['a','coddle','caalles','molly']
numbers=[10,20,30,40,50]
it=zip(words,numbers)

lst=list(it)
print(lst)

it=zip(words,numbers)
tpl=tuple(it)
print(tpl)

it=zip(words,numbers)
s=set(it)
print(s)
