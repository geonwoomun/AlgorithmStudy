# 백준 10844번 
from sys import stdin

input = stdin.readline

N = int(input())

dp = [[1 for i in range(10)] for _ in range(N+1)] # 0은 무시하는거고, 1부터 9까지 1로 채움. 계단 1개씩으로 인정하기 때문에
mod = 1000000000 # 나눌 값.

for i in range(2, N+1):   
    for j in range(10):
        if(j == 0):    
            dp[i][0] = dp[i-1][1] % mod # 뒤에 숫자가 0일 때는 그전의 1 값일 때를 더한 값. 
        elif(j == 9): # 9일 때는 8일 때를 더한 값.
            dp[i][j] = dp[i-1][8] % mod
        else: # 아니면 뒤가 -1 때와 +1일 때를 더한 값.
            dp[i][j] = (dp[i-1][j-1]+dp[i-1][j+1]) % mod


print((sum(dp[N]) - dp[N][0]) % 1000000000)
