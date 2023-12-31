'''import json
f=open('sampledata','w+')
lst=[10,20,30,40,50,60,70,80,90,100]
json.dump(lst,f)
f.seek(0)
inlst=json.load(f)
print(inlst)
f.close()'''

''' f=open('sampledata','w+')
lst=[10,20,30,40,50,60,70,80,90,100,110]
f.write(str(lst))
f.seek(0)
#d=f.readline()
m=f.read()
#print(d)
print(m)
f.close() '''

'''import json
f=open('sampledta1','w+')
tpl=('ajay',23,2455.55)
json.dump(tpl,f)
f.seek(0)
intpl=json.load(f)
#print(tuple(intpl))
print(intpl)
f.close()'''

import json
f=open('sampledta','w+')
dict={'ajay':23,'ajay':24,'nisha':55}
json.dump(dict,f)
f.seek(0)
intpl=json.load(f)
print(intpl)
f.close()