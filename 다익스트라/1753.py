from sys import stdin
import heapq

input = stdin.readline

V, E = map(int,input().split())
start = int(input())

INF = 10 * V + 1
distance = [[] for _ in range(V+1)]

for i in range(E):
    u, v, w = map(int, input().split())
    distance[u].append([v, w])

queue = []
start_distance = [INF for _ in range(V+1)]
start_distance[start] = 0
heapq.heappush(queue, [0, start])

while queue:
    mid = heapq.heappop(queue)
    for end in distance[mid[1]]:
        if start_distance[end[0]] > mid[0] + end[1]:
            start_distance[end[0]] = mid[0] + end[1]
            heapq.heappush(queue, [start_distance[end[0]], end[0]])

for i in range(1, V+1):
    if start_distance[i] == INF:
        print('INF')
    else:
        print(start_distance[i])


