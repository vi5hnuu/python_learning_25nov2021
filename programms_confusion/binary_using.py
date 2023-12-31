s='1011'
print(int(s,2))

i=0;
while s:
    i=i*2+(ord(s[0])-ord('0'))
    s=s[1:]
print(i)


print(ord('0'))