def encrypt(f1,f2):
    data=f1.read()
    for ch in data:
        f2.write(chr(ord(ch)+1))
def decrypt(f1,f2):
    data=f1.read()
    for ch in data:
        f2.write((chr(ord(ch)-1)))

source=input("Enter source file name :")
target=input("Enter target file name :")
f1=open(source,'r',encoding='utf-8')
f2=open(target,'w',encoding='utf-8')
ch=input("Encrypt or decrypt(E/D):")
if ch.upper()=='E':
    encrypt(f1,f2)
elif ch.upper()=='D':
    decrypt(f1,f2)
else:
    print("Enter valid choice")
f1.close()
f2.close()