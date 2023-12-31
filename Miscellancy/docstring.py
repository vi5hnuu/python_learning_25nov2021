def display():
    '''Display a message'''
    print('hello')
    print(display.__doc__)

def show(msg1='',msg2=''):
    '''display two messages

    arguments:
    msg1--messsage to diplay in lowecase (default='')
    msg2--messsage to diplay in uppercase (default='')
    '''
    print(msg1.lower())
    print(msg2.upper())
    print(show.__doc__)

display()
show('vishnu','kumar')
help(display)
help(show)