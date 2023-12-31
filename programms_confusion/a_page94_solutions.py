def fun1(d):
    if(d['type']=='dog'):
        return d['age']
    else:
        return 0

def fun2(n):
    if n==0:
        return False
    else:
        return True

dct={'A101':{'type':'cat','name':'tauby','age':6},'A102':{'type':'dog','name':'tommy','age':8},
     'A103':{'type':'dog','name':'tiger','age':10}
     }
#print(list(dct.values()))
