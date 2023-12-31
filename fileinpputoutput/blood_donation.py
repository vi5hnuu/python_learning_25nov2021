donors={'sanjay':['gokulpeth',25,1],
        'sunil':['shankarnagar',26,2],
        'akash':['sitaburdi',27,3],
        'rahul':['ramnagar',23,2],
        'riddhi':['dharampeth',22,2],
        'mangal':['ramdashpeth',21,2],
        }

f=open('donors.txt','w+')
for k,v in donors.items():
    s='{0:20}{1:40}{2:2}{3:1}\n'.format(k,v[0],str(v[1]),str(v[2]))
    f.write(s)
f.seek(0,0)
while True:
    data=f.readline()
    if data=='':
        break
    nam=data[:20]
    address=data[21:60]
    age=int(data[60:62])
    bloodtype=int(data[62:])
    if age<25 and bloodtype==2:
        print(nam,address,age,bloodtype)
f.close()