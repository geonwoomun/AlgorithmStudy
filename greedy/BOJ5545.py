# BOJ 5545번 최고의 피자
import sys

N = int(sys.stdin.readline()) # 토핑 종류의 수

A, B = map(int, sys.stdin.readline().split()) # 도우의 가격 A, 토핑의 가격 B

C = int(sys.stdin.readline()) # 도우의 열량 C

D = []

for i in range(N):
    D.append(int(sys.stdin.readline()))


price = A  # 가격들
kal = C # 칼로리들
MAX = kal / price  # 가격당 칼로리
result = MAX # 결과로 낼 변수.. 
D.sort(reverse=True)
# 칼로리가 큰 순으로 정렬한다음. 가격당 칼로리가 높을 때의 값을 result에 넣고
# int화 하면 내림이 되므로 출력.
for value in D : 
    kal += value
    price += B
    MAX = kal / price
    result = max(result, MAX)

print(int(result))

