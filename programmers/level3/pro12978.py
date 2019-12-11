# 프로그래머스 서머코딩/윈터코딩 배달  위에께 내것인데 테스트케이스 32번만 시간초과뜸...ㅠㅠ

# from collections import defaultdict, deque
    
# def solution(N, road, K):
#     dic = defaultdict(deque)
#     for v in road:
#         dic[v[0]].append((v[1], v[2]))
#         dic[v[1]].append((v[0], v[2]))
#     visit = set()
#     visit.add(1)
#     count = 1         
#     def dfs(start, dist, no, count) :
#         for c in dic[start]:
#             if c[0] != no and dist + c[1] <= K:
#                 if c[0] not in visit :
#                     visit.add(c[0])
#                     count +=1
#                 count = dfs(c[0],c[1]+dist, start, count)
#         return count
#     count = dfs(1,0,0,count) # 시작점, 거리, 이거 아닐 때 즉 되돌아 오는게 아닐때.,
#     return count

import math
from collections import deque
def bfs(start, maps, distance, K):
    queue = deque()
    queue.append(start)

    distance[start] = 0

    while queue:
        y = queue.popleft()
        for x in range(1, len(maps)):
            if maps[y][x] != 0:
                if distance[x] > distance[y] +maps[y][x] and distance[y]+maps[y][x] <= K:
                    distance[x] = distance[y] + maps[y][x]
                    queue.append(x)
    return len([i for i in distance if i <= K])

def solution(N, road, K):
    distance = [math.inf for _ in range(N+1)]
    maps = [[0 for _ in range(N+1)] for _ in range(N+1)]

    for frm, to, w in road:
        if maps[frm][to] == 0 and maps[to][frm] == 0:
            maps[frm][to], maps[to][frm] = w,w
        else:
            if w < maps[frm][to]:
                maps[frm][to] , maps[to][frm] = w, w
    return bfs(1, maps, distance, K)

road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
N= 6
K = 4
print(solution(N, road, K))