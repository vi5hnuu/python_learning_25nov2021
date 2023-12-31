# msg1='pay the taxes with smile...\n'
# msg2='pay the taxes with smile...\n'
# msg3='pay the taxes with smile...\n'
# msg4='pay the taxes with smile...\n'
# f= open('messages','w')
# f.write(msg1)
# f.write(msg2)
# f.write(msg3)
# f.write(msg4)
# f.close()
# f=open('messages','r')
# a=f.read()
# print(a)

# msg1='pay the taxes with smile...\n'
# msg2='pay the taxes with smile...\n'
# msg3='pay the taxes with smile...\n'
# msg4='pay the taxes with smile...\n'
# f= open('messages','w')
# # f.write(msg1,msg2,msg3,msg4)
# f.close()
# f=open('messages','r')
# a=f.read()
# print(a)

msg1='pay the taxes with smile...\n'
msg2='pay the taxes with smile...\n'
msg3='pay the taxes with smile...\n'
msg4='pay the taxes with smile...\n'
c=[msg1,msg2,msg3,msg4]
f= open('messages','w')
f.writelines(c)
f.close()
f=open('messages','r')
a=f.read()
print(a)