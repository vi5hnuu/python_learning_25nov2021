emp={'A101':{'name':'ashish','age':30,'salary':21000},
    'B102':{'name':'dinesh','age':25,'salary':12200},
    'A103':{'name':'ramesh','age':28,'salary':11000},
    'D104':{'name':'akhil','age':30,'salary':18000}}

d1={k:v for (k,v) in emp.items() if k.startswith('A')}
d2={k:v['name'] for (k,v) in emp.items()}
d3={k:v['age'] for (k,v) in emp.items()}
d4={k:v['age'] for (k,v) in emp.items() if v['age']>30}
d5={k:v['name'] for (k,v) in emp.items() if v['name'].startswith('a')}
d6={k:v['salary'] for (k,v) in emp.items() if v['salary']>13000 and v['salary']<=20000}
print(d1,d2,d3,d4,d5,d6,sep='\n')
