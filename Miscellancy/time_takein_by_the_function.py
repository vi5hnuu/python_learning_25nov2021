import time

def timer(func):
    def calculate(*arg,**kwargs):
        start_time=time.perf_counter()
        vale=func(*arg,**kwargs)
        end_time=time.perf_counter()
        runtime=end_time-start_time
        print(f'Finished{func.__name__!r} in {runtime:.8f} secs')
        return vale
    return calculate

@timer
def product(num,i):
    fact=i
    for i in range(num):
        fact=fact*i+1
    return fact

product(10,i=1)
