# import json
# import operator
#
# dct={'rakesh':25,'sameer':30,'suresh':33,'sanjay':25,'prabhu':22,'anil':23}
# f=open('stud_record','w+')
# json.dump(dct,f)
# f.seek(0)
# print(json.load(f))
# f.close()
#
# f=open('stud_record','r')
# dct={}
# while True:
#     data=f.readline()
#     # print(data)
#     if data=='':
#         break
#     stud=data.split()
#     # print(stud)
#     dct[stud[0]]=stud[1]
# f.close()
# print(dct)

import json
import operator

dct={'rakesh':25,'sameer':30,'suresh':33,'sanjay':25,'prabhu':22,'anil':23}
f=open('stud_record','w+')
json.dump(dct,f)
f.seek(0)
y=json.load(f)
for x,s in sorted(y.items(),key=operator.itemgetter(1),reverse=True):
    print(f'{x:<10}{s:>10}')

f.close()