f=open('para_replace','w')
s="She looked at her little \
girl who was about to become a teen.\
 She tried to think back to when the girl\
  had been younger but failed to pinpoint\
   the exact moment when she had become a\
    little too big to pick up and carry.\
     It hit her all at once. She was no longer\
      a little girl and she stood there speechless\
       with fear, sadness, and pride all running\
        through her at the same time."
f.write(s);
f.close()

f=open('para_replace','r')
for x in range(len(s)//50):
    data=f.read(50)
    data=data.replace('a',' ')
    data=data.replace('an',' ')
    data=data.replace('the',' ')
    print(data)
f.close()
