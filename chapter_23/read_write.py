msg1='Pay tax with a smile...\n'
msg2='I tried, but they wanted  money!\n'
msg3='Don\'t feel bad...\n'
msg4='It is alright to have no talent!\n'
f=open('messages','w')
f.write(msg1)
f.write(msg2)
f.write(msg3)
f.write(msg4)
f.close()
f=open('messages','r')
data=f.read()
print(data)
f.close()