words=['a','coddle','caalles','molly']
numbers=[10,20,30,40,50]
it=zip(words,numbers)
lst=list(it)
w,n=zip(*lst)
print(w)
print(n)