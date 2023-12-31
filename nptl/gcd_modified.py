def gcd(m,n):
    c=[x for x in range(1,m+1) for y in range(1,n+1) if m%x==0 and n%y==0 and x==y]
    print(max(c))

gcd(14,63)
