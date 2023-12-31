lst=['subham','nisha','sudha',('suresh',),('rajesh',),'radha']
boys=0
girls=0
for ele in lst:
    if isinstance(ele,tuple):
        boys+=1;
    else:
        girls+=1;
print('boys = ',boys,'girls = ',girls)