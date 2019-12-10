# 백준 2193번 이친수
# 예전에 풀려고 할 때는 무슨 말인지 잘 못 알아들어서 못 풀었었는데 
# 규칙을 찾아보니 역시 dp 문제 ... 규칙이 있다 점화식을 제대로 세우면 된다!

from sys import stdin
input = stdin.readline

N = int(input())

dp = [1 for _ in range(N)]

for i in range(2,N):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[N-1])