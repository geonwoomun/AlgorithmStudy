#BOJ 1912 연속합.

from sys import stdin
input = stdin.readline

n = int(input())

dp = list(map(int, input().split()))

maxs = dp[0]

for i in range(1, n): 
    if(dp[i-1] > 0 and dp[i-1]+dp[i] > 0):
        dp[i] += dp[i-1]
    if(maxs < dp[i]):
        maxs = dp[i]

print(maxs)