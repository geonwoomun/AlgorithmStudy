# 백준 2161번 카드
from collections import deque
from sys import stdin
input = stdin.readline

N = int(input())
q = deque()
for i in range(1,N+1):
    q.append(i)

while(not len(q) == 1):
    print(q.popleft(), end=" ")
    q.append(q.popleft())

print(q.popleft())


