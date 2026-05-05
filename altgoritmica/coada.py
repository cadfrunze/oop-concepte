from collections import deque


coada: deque = deque()
coada.append(1)
coada.append(2)
coada.append(3)

print(coada)
print(type(coada))
print(coada.popleft())
print(coada)