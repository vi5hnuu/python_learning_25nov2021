def gcd(m,n):
    if(m<n):
        m,n=n,m
        # print(m,n)
        # print(m-n)
    while(m%n!=0):
        diff=m-n
        (m,n)=(max(n,diff),min(n,diff))
    return n
print(gcd(14,63))
