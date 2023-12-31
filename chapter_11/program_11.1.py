'''students={'anil':23,'sanjay':28,'ajay':25}
stud=students
students={}
print(stud)'''

students={'anil':23,'sanjay':28,'ajay':25}
stud=students.copy() #deep copy
students={}
print(stud)