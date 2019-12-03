# BOJ 11403번 경로찾기

from collections import defaultdict, deque
import sys

N = int(sys.stdin.readline())
li = []
for _ in range(N):
    li.append(list(map(int,sys.stdin.readline().split())))
table = defaultdict(list)

for i in range(N):
    for j in range(N):
        if(li[i][j] == 1):
            table[i+1].append(j+1)

answer = [[0 for _ in range(N)] for _ in range(N)]

def bfs(start):
    q = deque()
    q.append(start)
    while q :
        a = q.popleft()
        for neighbor in table[a]:
            if answer[start-1][neighbor-1] == 0:
                answer[start-1][neighbor-1] = 1
                q.append(neighbor)


for i in range(1, N+1):
    bfs(i)
for i in range(N):
    for j in range(N):
        if(j == N-1):
            print(answer[i][j])
        else : print(answer[i][j], end = " ")