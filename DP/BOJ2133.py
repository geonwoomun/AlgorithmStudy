# BOJ 2133번 타일채우기

from sys import stdin
input = stdin.readline

N = int(input())

dp = [0 for _ in range(N+1)]

dp[0] = 1
dp[1] = 0   # 1줄은 못채운다.
if(N > 1):
    dp[2] = 3  # 2줄은 3가지 방법 가능.

for i in range(3, N+1):
    dp[i] = 3*dp[i-2] # 2개마다..   # 1증가할 때 -2 전의 것의 3배 만큼 가능. 즉 홀수것은 안된다.. 계속 0개인듯 하지만
    j = 4
    while i-j >= 0: # j 4부터  4개가 모이면 특이한 모양 2개를 만들 수 있기 때문에
        dp[i] += 2* dp[i-j] # i-j 개의 개수에서 *2 한거 만큼의 개수가 더해진다. 
        j +=2 # 홀수번은 셀 필요 없다..

print(dp[N])