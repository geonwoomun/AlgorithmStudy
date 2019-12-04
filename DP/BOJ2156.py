# BOJ 2156 포도주 시식
from sys import stdin
input = stdin.readline

n = int(input())

fodo = []
for _ in range(n):
    fodo.append(int(input()))

dp = [0 for _ in range(n)]
dp[0] = fodo[0]
if(n > 1):
    dp[1] = fodo[0] + fodo[1]
for i in range(2,n):
    dp[i] = max(dp[i-2] + fodo[i], dp[i-3] + fodo[i-1]+ fodo[i], dp[i-1])
    # dp[i]에 들어갈 수 있는 녀석은 2번전에 먹고 지금은 먹은 친구,   
    # 3번전에 먹고 이전꺼랑 지금 먹은것, 한번전에 먹고 안 먹은 것. 중. 
    # 최고로 많이 마신게 현재에서 제일 많이 마실 수 있는 것. 
print(dp[n-1])