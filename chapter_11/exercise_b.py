import operator

students={'dipti':{'math':48,'eng':60,'hindi':95},
          'smriti':{'math':75,'eng':68,'hindi':89},
          'subodh':{'math':45,'eng':66,'hindi':87}}

topper_name=''
topper_marks=0
for nam,info in students.items():
    total=0
    for sub,marks in info.items():
        total=total+marks
    avg=int(total/3)
    students[nam]={'Total':total,'Average':avg}
    if avg>topper_marks:
        topper_name=nam
        topper_marks=avg
print(students)
print('topper of the class is ',topper_name)
print('topper_marks ',topper_marks)