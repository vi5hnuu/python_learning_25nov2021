s=input('Enter a string :')
freq={}
for ch in s:
    if ch in freq:
        freq[ch]+=1;
    else:
        freq[ch]=1
print("Count of all characters is ",freq)

for k,v in freq.items():
    print(k,':',end='')
    for i in range(0,v):
        print('*',end='')
    print()
