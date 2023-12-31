def generate_prime():
    def isprime(num):
        if num>1:
            if num==2:
                return True
            if(num%2==0):
                return  False
            for i in range(2,num//2):
                if num%i==0:
                    return  False
                else:
                    return True
        else:
            return False

    num=1;
    while True:
        if isprime(num):
            yield num
        num+=1

total=0;
for x in generate_prime():
    if x<300000:
        total+=x;
    else:
        print(total)
        break