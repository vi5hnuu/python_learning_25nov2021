
S='vishnuss kumarrs'
print(tuple(sorted(set(S),key=S.index)))
print(tuple(sorted(set(S))))
print(list(sorted(set(S))))
print(list(sorted(set(S),key=S.index)))
print(''.join(sorted(set(S),key=S.index)))
print(sorted(S))