def fun(name='sanjay',age=25):
    print('name{0:>10}\nage{1:>10}'.format(name,age))
d={'name':"vishnu",'age':20}
fun(*d)
fun(**d)
