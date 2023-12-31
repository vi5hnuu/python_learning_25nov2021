def encrypt(f1,f2):
    s1='`1234567890-=!@#$%^&*()_+qwertyuiop[]QWERTYUIOP{}asdfghjkl;\'ASDFGHJKL:"zxcvbnm,./ZXCVBNM<>?'
    s2='\'ASDFGHJKL:"ZXCVBNM,./ZXCVBNM<>?`1234567890-=!@#$%^&*()_+QWERTYUIOP{}asdfghjkl;'
    data=f1.read()
    for ch in data:
        pos=s1.find(ch);
        if pos==-1:
            f2.write(ch)
        else:
            f2.write(s2[pos])
def decrypt(f1,f2):
    s1='`1234567890-=!@#$%^&*()_+qwertyuiop[]QWERTYUIOP{}asdfghjkl;\'ASDFGHJKL:"zxcvbnm,./ZXCVBNM<>?'
    s2='\'ASDFGHJKL:"ZXCVBNM,./ZXCVBNM<>?`1234567890-=!@#$%^&*()_+QWERTYUIOP{}asdfghjkl;'
    data=f1.read()
    for ch in data:
        pos=s2.find(ch)
        if pos==-1:
            f2.write(ch)
        else:
            f2.write(s1[pos])

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
