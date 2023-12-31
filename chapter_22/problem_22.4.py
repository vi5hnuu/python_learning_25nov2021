while True:
    try:
        num=int(input('Enter a number : '))
        break
    except ValueError:
        print('incorrect input')
print('you Entered ',num)