def convert(s1):
    itt=[s for s in s1.split('-')]
    itt.sort() #sort original items
    s2='-'.join(itt)
    return s2

s='here-come-the-dots-followed-by-dashes'
t=convert(s)
print(t)