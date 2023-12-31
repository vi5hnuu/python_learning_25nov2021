try:
    a=int(input("enter no:"))
    b=int(input("enter no:"))
    print(a/b)
except ZeroDivisionError:
    print('second arg cant be zero')