# BOJ 11724 연결 요소의 개수
# 백준 것은 아무래도 input()으로 받는 것보다 sys.stdin.readline()으로 받는게 맞는 것 같다.
# input()으로 하면 시간 초과 떴는데 sys.stdin.readline()하니깐 시간초과 안 뜸. 
# input()으로 할 때는 python3 는 시간초과나 런타임에러 뜨고 pypy3만 됨....
# 배열로 할 때랑 조금 다른 느낌이라 헷갈렸지만 이제 알았다.
# 받은거를 인덱스에 따라 잘 넣어두고 dfs 든 bfs든 하면 될듯
# 방향이 없는 것이기 때문에 두군데 다 넣어야함.

import sys
sys.setrecursionlimit(1000000)

def dfs(i): # 방문했다고 체크하고 그것의 vertex[i]에 있는 녀석들이 방문 안한 녀석이면 dfs 진행.
    node[i] = True
    for value in vertex[i]:
        if(not node[value]):
            dfs(value)

N, M = map(int, sys.stdin.readline().split())

node = [False for i in range(N+1)] # 방문 한곳인지 아닌지 체크 하는 것.
vertex = [[] for i in range(N+1)] # 각 노드마다 어디로 갈 수 있는지를 index 마다 리스트를 만든다.
count = 0
for i in range(M):
    a,b = map(int, sys.stdin.readline().split()) # 방향이 없기 때문에 두군데 다 넣음.
    vertex[a].append(b)
    vertex[b].append(a)

for i in range(1, len(node)):
    if not (node[i]): # 노드로 시작해서 아직 방문 안 한 애면 count 1을 늘리고 dfs 시작.
        count += 1
        dfs(i)
        
print(count)

# 딕셔너리로 해본것.
# N, M = map(int, sys.stdin.readline().split())

# node = [False for i in range(N+1)]
# vertex = {}
# for i in range(1, N+1):
#     vertex[i] = []
# count = 0
# for i in range(M):
#     a,b = map(int, sys.stdin.readline().split())
#     vertex[a].append(b)
#     vertex[b].append(a)

# def dfs(i):
#     node[i] = True
#     for j in range(len(vertex[i])):
#         v1 = vertex[i][j]
#         if(not node[v1]):
#             dfs(v1)

# for i in range(1, len(node)):
#     if(not node[i]):
#         count += 1
#         dfs(i)
        
# print(count)