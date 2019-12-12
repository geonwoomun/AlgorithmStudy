# BOJ 1389 케빈 베이컨의 6단계 법칙
from collections import defaultdict, deque
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())

dic = defaultdict(deque)

for i in range(M):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

def bfs(i,dist):
    q = deque()
    q.append((i,dist))
    visit.add(i)
    kvNum = 0
    while q:
        x, d = q.popleft()
        for v in dic[x]:
            if v not in visit:
                visit.add(v)
                kvNum += d+1
                q.append((v, d+1))
    return kvNum

mins = 10000000
index = 1
for i in range(1, N+1):
    visit = set()
    kvNum = bfs(i,0)
    if mins > kvNum:
        mins = kvNum
        index = i

print(index)


