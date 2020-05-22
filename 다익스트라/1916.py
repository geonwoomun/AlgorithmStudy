from sys import stdin
import heapq

input = stdin.readline

N = int(input())
M = int(input())


INF = 100000 * N + 1
costs = [[] for _ in range(N + 1)]

for i in range(M):
    start, end, cost = map(int, input().split())
    costs[start].append([end, cost])

start, end = map(int, input().split())

queue = []
start_cost = [INF for _ in range(N + 1)]
start_cost[start] = 0
heapq.heappush(queue, [start, 0])

while queue:
    s, s_cost = heapq.heappop(queue)
    for e, e_cost in costs[s]:
        if start_cost[e] > e_cost + s_cost:
            start_cost[e] = e_cost + s_cost
            heapq.heappush(queue, [e, start_cost[e]])

print(start_cost[end])
