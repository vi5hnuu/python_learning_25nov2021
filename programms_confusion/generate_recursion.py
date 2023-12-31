# def generate(n):
#     lol=list()
#     for x in range(1,n+1):
#         for y in range(1,n+1):
#             for z in range(1,n+1):
#                 if(x!=y and y!=z and x!=z):
#                     t=[x,y,z]
#                     lol.append(t);
#                 else:
#                     pass
#     print(lol)
# generate(3)

# def generate(n):
#     lol=[[x,y,z] for x in range(1,n+1) for y in range(1,n+1) for z in range(1,n+1) if (x!=y and y!=z and z!=x)]
#     print(lol)
# generate(3)

#chk...generate1.py for ecursion