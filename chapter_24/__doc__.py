def display():
    '''display message'''
    print('hello')
    print(display.__doc__)

def show(msg1='',msg2=''):
    '''display 2  message

     argument:
     msg1--msg to be displayed in lowercase (default='')
     msg2=--msgb to be displayed in uppercase (default='')'''

    print(msg1.lower())
    print(msg2.upper())
    print(show.__doc__)

display()
show('cindrela','mozerella')
help(display)
help(show)