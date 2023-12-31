name="vishnu"
salery="0"
age=20
agee=20.2
#using f
print(f"name is {name} and age is {age} and slaery is {salery} ")
print(f"name is {name:10} and age is {age:10} and slaery is {salery:10} ")
#using format
print("name is {} and age is {} and salery is {}".format(name,age,salery))
print("name is {0} and age is {1} and salery is {2}".format(name,age,salery))
print("name is {0:10} and age is {1:10} and salery is {2:10}".format(name,age,salery))
print("name is {0:10} and age is {1:10.2} and salery is {2:10}".format(name,agee,salery))
print("name is {0:10} and age is {1:10.2f} and salery is {2:10}".format(name,agee,salery))

a,b,c=2,3,4;
print(f"{a:10}{b:10}{c:10}")
print(f"{a:>10}{b:>10}{c:>10}")
print(f"{a:^10}{b:<10}{c:<10}") #> right justified,< left justified ,^ centre justified