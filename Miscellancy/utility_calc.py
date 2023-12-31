import sys

if len(sys.argv)!=4:
    print('incorrect usage')
    print('calc operator number number')
    sys.exit(1)

operator=sys.argv[1]
m=int(sys.argv[2])
n=int(sys.argv[3])
if operator=='+':
    result=m+n
    print('sum :',result)
elif operator=='-':
    result=m-n
    print('substraction :', result)
elif operator=='*':
    result=m*n
    print('multiplication :', result)
elif operator=='/':
    result=m/n
    print('true_division :', result)
elif operator=='//':
    result=m//n
    print('floor_division :', result)
else:
    print('illegal operator')
