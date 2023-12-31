f=open('file_a','w')
s=['vishnu\n','krishan\n','pooja\n','prakash\n','laxmi\n']
f.writelines(s);
f.close()
f=open('file_a','r')
i=0
while True:
    data=f.readline()
    i=i+1
    if data=='':
        break
    print(f'{i:<5}',data)
f.close()