# 백준 9465번 스티커

from sys import stdin
input = stdin.readline

T = int(input())

while(T > 0):
    n = int(input())
    sticker = [list(map(int, input().split())) for i in range(2)]
    dp = [[0 for _ in range(n)] for i in range(2)]

    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    if(n > 1):
        dp[0][1] = sticker[1][0] + sticker[0][1] 
        dp[1][1] = sticker[0][0] + sticker[1][1]
    maxA = max(max(dp[0]), max(dp[1]))
    for j in range(2, n): # 0 일때는 1일 때의 그전 것과 그전전 것 중 큰거를 더해야함. 그래야 최대가 됨..
        dp[0][j] = max(dp[1][j-1], dp[1][j-2]) + sticker[0][j] 
        dp[1][j] = max(dp[0][j-1],dp[0][j-2]) + sticker[1][j] # 1일 때는 0일 때 의 그전과 그전전 중 큰 것.
        maxA = max(maxA, max(dp[0][j], dp[1][j]))
    print(maxA)
    T -=1
