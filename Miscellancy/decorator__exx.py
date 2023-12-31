def calldecorator(func):
    def decorated(*args,**kargs):
        print(f'calling {func.__name__}({args},{kargs})')
        ret=func(*args,**kargs)
        print(f'called {func.__name__} ({args},{kargs}) got ret value: {ret}')
    return decorated()

@calldecorator
def sum_sum(a,b):
    return (a+b)

@calldecorator
def sum_summ(a,b,c):
    return (a+b+c)

sum_sum(10,5)
sum_summ(10,5,2)
