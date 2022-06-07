nums=[1,2,3,4,5,6,7]
k=3

from collections import deque

q = deque(nums)

for i in range(k):
    q.appendleft(q.pop())

print(q)
