s='The Terrible Tiger Tore The Tower'
pos=s.find('T',0)
print(pos,s[pos])
pos=s.find('T',pos+1)
print(pos,s[pos])
pos=s.find('T',pos+1)
print(pos,s[pos])
pos=s.find('T',pos+1)
print(pos,s[pos])
pos=s.find('T',pos+1)
print(pos,s[pos])
pos=s.find('T',pos+1)
print(pos,s[pos])
pos=s.find('T',pos+1)
print(pos)
c=s.count('T')
s=s.replace('T','t',c)
print(s)



