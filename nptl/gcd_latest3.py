def gcd(m,n):
    if(m<n):
        m,n=n,m
        # print(m,n)
        # print(m-n)
    if(m%n==0):
        return n
    else:
        diff=m-n;
        return(gcd(max(n,diff),min(n,diff)))
print(gcd(14,63))
