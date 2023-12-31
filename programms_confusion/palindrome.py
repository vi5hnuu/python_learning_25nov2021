def palindrome(s):
    #if s[::-1]==s[:]:
    if ''.join(list(reversed(s)))==s[:]:
        print("palindrome")
    else:
        print("not")


s="malalylalam"
palindrome(s)
print(sorted(s))
print(''.join(list(reversed(s))))