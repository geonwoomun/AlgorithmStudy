# 타일 붙이기
# 역시 점화식을 잘 세우면 됨.
T = int(input())

for t in range(1, T+1):
    N = int(input())
    dp = [0 for i in range(N+1)]
    dp[1] = 1
    dp[2] = 3
    dp[3] = 6
    for i in range(4, N+1):
        dp[i] = dp[i-1] + 2*dp[i-2] + dp[i-3]
    
    print("#", end="")
    print(t, dp[N])