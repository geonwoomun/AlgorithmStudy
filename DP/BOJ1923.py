# BOJ 1923 정수삼각형

from sys import stdin
input = stdin.readline

n = int(input())
dp = []
for i in range(n):
    dp.append(list(map(int, input().split())))


for i in range(n-2, -1, -1): # 거꾸로 가면서 계산.
    for j in range(len(dp[i])):
        dp[i][j] = max(dp[i+1][j] , dp[i+1][j+1]) + dp[i][j]

print(dp[0][0])