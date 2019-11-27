# 백준 2589 보물섬

# collections의 deque로 하면 일반 list보다 속도가 빠름.
# 그 값 안에 있는 원소가 바뀌지 않는 녀석일 때는 tuple (1,2,3,4) 이런식으로 만드는게 더 빠르다.
# cx, cy를 [](리스트) 로 만들었을 때는 시간초과가 뜨는데 이것만 ()로 고쳐도 시간초과가 안 뜸.
# 조금의 차이로 시간초과가 뜨고 안 뜨고가 되는 듯.
import sys
from collections import deque # 덱, 큐와 스택을 두개다 할 수 있는 것.
n, m = map(int, sys.stdin.readline().split())

maps = [list(sys.stdin.readline()) for i in range(n)]

cx = (0, 0, 1, -1) # tuple로 만들어 놓는게 빠르다.
cy = (1, -1, 0, 0)
maxRange = 0
Q = deque()

def Bfs(i, j):
    visit[i][j] = True
    Q.append((i, j, 0)) # 거리까지 같이 넣는 듯. i , j, 거리 넣어서 다음 것일 때마다 거리 + 1 시킨다. 여기도 튜플로 만들어 넣는게 빠름. 튜플 자체를 추가하고 뺄게 아니기 때문에.
    maxRange = 0 # 그중에 최대를 리턴 할 것임.
    while Q: # 큐가 있을 때.
        x, y, d = Q.popleft() # 큐에서 꺼낸걸 하나씩 넣음. popleft가 맨 왼쪽껄 빼는것
        for i in range(4):
            a = x + cx[i]
            b = y + cy[i]
            if(a>=0 and a <n and b >=0 and b < m and maps[a][b] == 'L' and visit[a][b] is False):
                Q.append((a, b, d+1))
                visit[a][b] = True
                maxRange = max(maxRange, d+1)
    return maxRange

for i in range(n):
    for j in range(m):
        if(maps[i][j] == 'L'):
            visit = [[False]*m for i in range(n)] # visit 초기화.
            maxRange = max(maxRange, Bfs(i,j)) # 현재 값이랑 Bfs를 해서 나온 최대값을 반환.

print(maxRange)