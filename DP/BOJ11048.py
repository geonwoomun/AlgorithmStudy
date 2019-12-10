# BOJ 11048 이동하기

from sys import stdin
input = stdin.readline

N, M = map(int, input().split())

candys = []

for i in range(N):
    candys.append(list(map(int,input().split())))

for i in range(N):
    for j in range(M):
        if(i > 0 and j > 0):
            candys[i][j] = max(candys[i][j-1], candys[i-1][j], candys[i-1][j-1]) + candys[i][j]
        elif(i>0):
            candys[i][j] =candys[i-1][j] + candys[i][j]
        elif(j>0):
            candys[i][j] =candys[i][j-1] + candys[i][j]

print(candys[N-1][M-1])