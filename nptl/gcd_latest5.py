def gcd(m,n):
    if(m<n):
        m,n=n,m
        # print(m,n)
        # print(m-n)
    if(m%n==0):
        return n
    else:
        r=m%n;
        return(gcd(n,r))
print(gcd(14,63))
