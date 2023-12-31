import operator

d={'oil':230,'clip':150,'stud':175,'nut':35}
print(sorted(d))
print(sorted(d.items()))
print(sorted(d.items(),reverse=True))
print(sorted(d.items(),reverse=True,key=operator.itemgetter(1)))
print(sorted(d.items(),reverse=False,key=operator.itemgetter(1)))