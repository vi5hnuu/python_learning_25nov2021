try:
    a=int(input("enter no:"))
    b=int(input("enter no:"))
    print(a/b)
except ZeroDivisionError as zde:
    print('second arg cant be zero')
    print(zde.args)
    print(zde)
except ValueError:
    print("Unable to convert string to int")
except:
    print("Unknown error")