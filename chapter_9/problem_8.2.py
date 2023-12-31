tpl=(10,20,30,40,50,60,70,80,90,100)
a,b,c,d,e,f,g,h,i,j=tpl
print(tpl)
print(a,b,c,d,e,f,g,h,i,j)
x,_,_,_,_,_,_,_,_,y=tpl
print(x,y,_)
i,*_,j=tpl
print(x,y,_)