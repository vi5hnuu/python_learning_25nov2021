string='Nagpur-440010'
alphabets=digits=special=0

for i in range(len(string)):
    if(string[i].isalpha()):
        alphabets=alphabets+1
    elif(string[i].isdigit()) :
        digits=digits+1;
    else :
        special=special+1
print('Alphabets : ',alphabets)
print('digits : ',digits)
print('special : ',special)