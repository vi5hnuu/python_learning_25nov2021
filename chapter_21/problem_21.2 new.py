def generate_prime():
    num=1
    while True:
        if isprime(num):
            return num
        num+=1
def isprime(n):
    if n>1:
        if n==2:
            return True

        if n%2==0:
            return False
        for i in range(2,n//2):
            if n%i==0:
                return False
            else:
                    return True
        else:
            return False
total=0;
for next_prime in generate_prime():
    if next_prime<300000:
        total+=next_prime
    else:
        print(total)
        exit() #check next program

'''
S.NO.	YIELD	RETURN
1	Yield is generally used to convert a regular Python function into a generator.	Return is generally used for the end of the execution and “returns” the result to the caller statement.
2	It replace the return of a function to suspend its execution without destroying local variables.	It exits from a function and handing back a value to its caller.
3	It is used when the generator returns an intermediate result to the caller.	It is used when a function is ready to send a value.
4	Code written after yield statement execute in next function call.	while, code written after return statement wont execute.
5	It can run multiple times.	It only runs single time.
6	Yield statement function is executed from the last state from where the function get paused.	Every function calls run the function from the start.
'''