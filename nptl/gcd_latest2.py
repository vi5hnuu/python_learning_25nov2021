def gcd(m,n):
    for x in range(abs(m-n),1,-1):
        if m%x==0 and n%x==0:
            print(x)
            break;
        else:
            pass
gcd(14,63)
