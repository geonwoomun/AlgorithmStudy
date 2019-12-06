# BOJ 6359번 만취한 상범

from sys import stdin
input = stdin.readline

T = int(input())

while T > 0 :
    n = int(input())
    dp = [0 for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(i, n+1, i):
            if(dp[j] == 0):
                dp[j] = 1
            else:
                dp[j] = 0
    print(dp.count(1))
    T -= 1 