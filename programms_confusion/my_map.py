def my_map(new_func,listt):
    a=[]
    for x in listt:
        a.append(new_func(x));

    return a;
z=[1,2,3,4,5]
listy=my_map(lambda x:x*x,z)
print(listy)
        