# 백준 9461번 파도반 수열
# 주어진 식에서 규칙을 찾아보니 처음에 111을 주고 그다음부터는 i-2 + i-3 == i 였다.
from sys import stdin
input = stdin.readline

T = int(input())


while T > 0:
    N = int(input())
    dp = [1 for _ in range(N)]

    for i in range(3,N):
        dp[i] = dp[i-2] + dp[i-3]
    
    print(dp[N-1])
    T -= 1