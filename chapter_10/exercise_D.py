import random
s=set()
while True:
    s.add(random.randint(15,45))
    if(len(s)==10):
        break
print('original set',s)
t=set()
count=0
for item in s:
    if item<30:
        count+=1;
    if item<=35:
        t.add(item)
s=t
print('Count of numbers less than 30',count)
print('Set after deleting elements > 35 :',s)