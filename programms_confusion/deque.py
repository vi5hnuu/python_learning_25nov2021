import collections

q=collections.deque()
q.append(10)
q.append(11)
q.append(12)
q.append(13)
q.append(14)
q.append(15)
q.append(16)
q.popleft()
q.popleft()
q.pop()

print(q)