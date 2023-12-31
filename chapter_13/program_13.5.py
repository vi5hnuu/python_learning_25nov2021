def ispalindrome(s):
    t=s.lower()
    for i in range(0,len(s)-1):
        if(s[i]==s[len(s)-1-i]):
            k='Palindrome'
        else :
            k='not Palindrome'
    return k
print(ispalindrome('aba'))
print(ispalindrome('abba'))
print(ispalindrome('abaa'))