words=['a','coddle','caalles','molly']
numbers=[10,20,30,40,50]

for ele in zip(words,numbers):
    print(ele[0],ele[1])

for ele in zip(words,numbers):
    print(*ele)

for e,f in zip(words,numbers):
    print(e,f)