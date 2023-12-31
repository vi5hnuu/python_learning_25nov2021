# class complex:
#     def __init__(self,r=0.0,i=0.0):
#         self.__real=r
#         self.__imag=i
#     def __eq__(self,other):
#         if(self.__real==other.__real and self.__imag==other.__imag):
#             return True
#         else:
#             return False
#
# c1=complex(1.1,0.2)
# c2=complex(0.4,2.1)
# c3=c1
# if c1==c2:
#     print("c1==c2");
# else:
#     print("c1!=c2")


class complex:
    def __init__(self,r=0.0,i=0.0):
        self.__real=r
        self.__imag=i

c1=complex(1.1,0.2)
c2=complex(0.4,2.1)
c3=c1
if type(c1)==type(c2):
    print("c1==c2");
else:
    print("c1!=c2")

if c1 is c3:
    print("c1==c3")
else:
    print("c1!=c3")

