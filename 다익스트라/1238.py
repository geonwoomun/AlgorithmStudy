from sys import stdin
import heapq

input = stdin.readline

# N 마을, M 개의 단방향 도로 I번째 길을 지나는데 T1의 시간
# 집에서 X에 갈 수 있고, X에서 집으로 돌아올수 있는 데이터만 입력..


# 도로의 시작점, 끝점 그리고 필요한 시간
def dij(temp, result, X):
    queue = []
    result[X] = 0
    heapq.heappush(queue, [0, X])

    while queue:
        s_time, s = heapq.heappop(queue)
        for e_time, e in temp[s]:
            if result[e] > e_time + s_time:
                result[e] = e_time + s_time
                heapq.heappush(queue, [result[e], e])


INF = 1e9
N, M, X = map(int, input().split())

distance = [[] for _ in range(N + 1)]
x_dist = [INF] * (N + 1)
r_distance = [[] for _ in range(N + 1)]
r_x_dist = [INF] * (N + 1)

for i in range(M):
    s, e, t = map(int, input().split())
    distance[s].append([t, e])
    r_distance[e].append([t, s])

dij(distance, x_dist, X)
dij(r_distance, r_x_dist, X)

for i in range(1, len(x_dist)):
    x_dist[i] += r_x_dist[i]

print(max(x_dist[1:]))
