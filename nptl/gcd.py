def gcd(m,n):
    a=[x for x in range(1,m+1) if m%x==0]
    b=[y for y in range(1,n+1) if n%y==0]
    # print(a,b)
    c=[x for x in a for y in b if x==y]
    print(max(c))


# c=list(map(lambda x,y:[x,y],[1,2,3],[2,3,4]))
# print(c)
gcd(14,63)
