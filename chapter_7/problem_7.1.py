#r,l,b=input("Enter radius,length and bredth : ").split()
r,l,b=input("Enter radius,length and bredth : ").split(':')
radius=int(r)
length=int(l)
bredth=int(b)
circumference=2*3.14*radius
perimeter=2*(length+bredth)
print(circumference)
print(perimeter)