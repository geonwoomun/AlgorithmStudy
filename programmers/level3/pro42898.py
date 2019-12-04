# 프로그래머스 등굣길

def solution(m, n, puddles):
    answer = 0
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)] # 0 ~ m n까지 만들고 1부터 m n까지를 쓸거임.
    mod = 1000000007
    for v in puddles: # 웅덩이를 -1로 체크
        a,b = v
        dp[b][a] = -1

    dp[1][1] = 1 # 시작지점 0

    for i in range(1,n+1): # 1부터 n, m까지지
        for j in range(1,m+1):
            if(dp[i][j] == -1): # 웅덩이면 0으로 바꿔서 다음에 영향 안미치게해줌.
                dp[i][j] = 0
            else:
                dp[i][j] += (dp[i][j-1] + dp[i-1][j]) % mod # 1,1을 영향 안 받게 +=으로 해줌.

    return dp[n][m] % mod

m= 4
n = 3
puddles = [[2,2]]
print(solution(4,3,puddles))