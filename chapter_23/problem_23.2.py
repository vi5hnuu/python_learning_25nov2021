f=open('numbers','wb')
f.write(b'231')
f.write(b'232')
f.write(b'233')
f.write(b'234')
f.close()

f=open('numbers','rb')
f.seek(10,0)
print(f.tell())
f.seek(2,1)
print(f.tell())
f.seek(-5,1)
print(f.tell())
f.seek(-10,2)
print(f.tell())
f.close()