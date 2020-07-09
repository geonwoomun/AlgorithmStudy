from sys import stdin

input = stdin.readline

N = int(input())

t = []
p = []
dp = []

for i in range(N):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    dp.append(b)

for i in range(1, N):
    for j in range(i):
        if i - j >= t[j]:
            dp[i] = max(p[i] + dp[j], dp[i])

result = 0
for i in range(N):
    if(i + t[i] <= N):
        result = max(result, dp[i])

print(result)
