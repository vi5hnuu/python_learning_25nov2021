words={'tub':1,'toothbrush':2,'towel':3,'nailcutter':4}
d={''.join(a for a in k if a not in 'aeiouAEIOU'): v for (k,v) in words.items()}
print(d)
