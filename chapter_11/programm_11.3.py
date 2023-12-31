import operator
d={'oil':230,'clip':150,'stud':175,'nut':35}
print('Original dictonary ',d)

d1=sorted(d.items())
print('Asc. order by key',d1)

d2=sorted(d.items(),reverse=True)
print('Desc. order by key ',d2)

d3=sorted(d.items(),key=operator.itemgetter(1))
print('Asc. order by value',d3)

d3=sorted(d.items(),key=operator.itemgetter(1),reverse=True)
print('Desc. order by value',d3)