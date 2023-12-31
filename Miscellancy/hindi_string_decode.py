import sys
print(sys.stdin.encoding)

eng='A B C D'
dev='प र क त'
print(type(eng))
print(type(dev))
print(eng)
print(dev)

print(eng.encode('utf-8'))
print(eng.encode('utf-16'))
print(dev.encode('utf-8'))
print(dev.encode('utf-16'))

print(b'A B C D'.decode('utf-8'))
print(b'\xe0\xa4\xaa \xe0\xa4\xb0 \xe0\xa4\x95 \xe0\xa4\xa4'.decode('utf-8'))