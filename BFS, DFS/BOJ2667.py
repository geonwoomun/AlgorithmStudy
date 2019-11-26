# 백준 단지 번호 붙이기 
# dfs로 풀어보기 
import sys
sys.setrecursionlimit(100000)

N = int(input())

home = []
for i in range(N):
    home.append(list(map(int, input())))

cx = [0,0,1,-1]
cy = [1,-1,0,0]
count = 0

def dfs(i, j):
    home[i][j] = 0
    for k in range(4):
        x = i + cx[k]
        y = j + cy[k]
        if(x >= 0 and x < N and y >=0 and y < N and home[x][y] == 1):
            danji[-1] += 1
            dfs(x,y)

danji = []

for i in range(N):
    for j in range(N):
        if(home[i][j] == 1):
            danji.append(1)
            dfs(i,j)
            count += 1

print(count)
danji.sort()
for value in danji:
    print(value)