f=open('messages','r')
while True:
    data=f.read(1)
    if data=='':
        break
    print(data,end='+')

f.close()