# 백준 2164 카드2
from collections import deque
from sys import stdin
input = stdin.readline
N = int(input())
q = deque()
for i in range(1,N+1):
    q.append(i)

while not len(q) == 1:
    q.popleft()
    q.append(q.popleft())
print(q.popleft())
