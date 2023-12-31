def gcd(m,n):
    c=[x for x in range(1,min(m,n)+1)if m%x==0 and n%x==0]
    print(max(c))

gcd(14,63)
