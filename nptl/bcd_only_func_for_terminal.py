def gcd(m,n):
    if(m<n):
        m,n=n,m
        # print(m,n)
        # print(m-n)
    while(m%n!=0):
        # r=m%n;
        (m,n)=n,m%n
    return n

