import json
def encode_employee(x):
    if isinstance(x,employee):
        return (x.ecode,x.ename,x.doj,x.sal)
    else:
        raise TypeError("complex object is not seriliazatio compatible")
def decode_employee(dct):
    if '__emplyee__' in dct:
        return employee(dct['ecode'],dct['ename'],dct['doj'],dct['sal'])
    return dct

class employee:
    def __init__(self,ecode,ename,doj,sal):
        self.ecode=ecode
        self.ename=ename
        self.doj=doj
        self.sal=sal
    def print(self):
        print(self.ecode,self.ename,self.doj,self.sal)

e=employee('A101','sameer','17/11/2017',25000)
f=open('data','w+')
json.dump(e,f,default=encode_employee)
f.seek(0)
ine=json.load(f,object_hook=decode_employee)
print(ine)