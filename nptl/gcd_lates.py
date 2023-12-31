def gcd(m,n):
    for x in range(1,min(m,n)+1):
        if m%x==0 and n%x==0:
            gcdd=x
    print(gcdd)

gcd(14,63)
