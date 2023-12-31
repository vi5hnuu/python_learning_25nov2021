num=int(input('Enter how many number you wanna enter : '))
totalsum=0
number=[float(x) for x in input("Enter all numbers : ").split()]
for n in range(len(number)):
    totalsum=totalsum+number[n]
avg=totalsum/num;
print("Average of ",num," num                                                                                                                                                                                                                                           ber is ",avg)