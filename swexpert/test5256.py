# 이항계수 
# 이항계수의 성질을 알아야한다고 할까... 공식을 알아야함.
# nCm = n-1Cm-1 + n-1Cm 을 재귀적으로 + dp까지 써서 해야한다.
T = int(input())

def memo(i,j):
    if (dp[i][j] > 0) :        
        return dp[i][j]
    if j ==0 or i == j:
        dp[i][j] = 1
        return dp[i][j]
    
    dp[i][j] = memo(i-1, j-1) + memo(i-1, j)
    return dp[i][j]
     

for t in range(1, T+1):
    n, a, b = map(int, input().split())
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

    result = memo(n,n-a)
    print("#",end='')
    print(t, result)