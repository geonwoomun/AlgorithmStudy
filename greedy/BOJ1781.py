# BOJ 1781 컵라면
# 숙제의 개수가 많아서 그런가 배열로 하면 시간 초과가 나온다.
# 우선순위 큐를 사용해서 해야하는 것 같다!
# 데드라인 시간이 짧은거부터 그리고 컵라면 수가 많은 거부터로 정렬을 하였다.
# 데드라인을 재고 나서 일단 큐에 추가를 하고
# 데드라인 보다 큐의 길이가 길면 다 끝내지 못한다는 말이므로 제거했다. 우선순위 큐이므로
# 제거를 하면 제일 작은 수부터 제거 되었다.
# 그리고 큐가 비었을 때까지 더해서 sum을 출력하였다.

import sys
from queue import PriorityQueue
N = int(sys.stdin.readline())

cup = []

for i in range(N):
    cup.append(list(map(int, sys.stdin.readline().split())))

cup.sort(key=lambda x : (x[0], -x[1]))

result = PriorityQueue() # 컵라면의 개수들을 담을꺼임.
for c in cup:
    d = c[0]
    result.put(c[1])
    while(result.qsize() > d):
        result.get()

SUM = 0
while(not result.empty()):
    SUM += result.get()

print(SUM)