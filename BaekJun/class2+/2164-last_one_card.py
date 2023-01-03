from collections import deque
N = int(input())
dq = deque(range(1, N + 1))

while len(dq) != 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq.pop())

print("---------")
dq2 = deque([1,2,2,2,3,4,5,2,2,6])
print("before remove :", dq2)
dq2.remove(2)
print("after remove :", dq2)