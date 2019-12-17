# 5247 연산

from collections import deque

def bfs(start,end, count) : # bfs 함수
    q = deque()
    q.append((start, count))  # 튜플로 start, count 받음.
    while q:
        value, cnt = q.popleft() 
        if value == end: # 만약 지금 값이 원하는 값과 같다면 그 cnt를 반환. 제일 처음 걸렸을 때가 cnt가 가장 작을 때임.
            return cnt
        for i in range(4):
            if i == 0:
                temp = value + 1
            if i == 1:
                temp = value - 1
            if i == 2:
                temp = value * 2
            if i == 3:
                temp = value - 10  # 4개를 돌려서 모든 경우를 큐에 넣는다.
            if temp <= 1000000 and temp not in visit : # 단 값이 이 조건일 경우에만.
                    visit.add(temp)
                    q.append((temp, cnt+1))


T = int(input())

for t in range(1, T +1):
    start, end = map(int, input().split())
    visit = set()
    count = 0 # 횟수.
    visit.add(start) # 현재 값이 쓰였는지 안 쓰였는지 확인 하기 위함. 쓰였으면 다시 할 필요가 없는게 이미 앞에서 쓰인 값이 더 횟수가 적기 때문이다.
    result = bfs(start, end, count) # 시작값, 끝값, 시작 count를 변수로 넣어서 결과를 리턴 받음.
    print("#", end='')
    print(t, result)