import random
r={random.randint(15,45) for n in range(10)}
print(r)


t={int(15+30*random.random()) for n in range(10)}
print(t)
count=len({num for num in t if num<30})
print(count)
s={num for num in t if num<30}
t=t-s;
print(t)