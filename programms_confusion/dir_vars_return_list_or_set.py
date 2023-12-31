# print(vars(list))
# print(set(vars(list)))
print(vars(list).keys())
# print(set(vars(list).keys()))
print(dir(list))
print(set(dir(list)))
print(set(dir(list)).difference(vars(list).keys()))
print(set(dir(list)).difference(set(vars(list).keys())))


