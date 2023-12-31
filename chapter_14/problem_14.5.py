#dec to binary
import sys
def dec_to_binary(n):
    r=n%2
    n=int(n/2)
    if n!=0:
        dec_to_binary(n)
    print(r,end='')

sys.setrecursionlimit(10**6)
num=int(input("Enter the decimal number : "))
print("Binary equivalent : ",end='')
dec_to_binary(num)
