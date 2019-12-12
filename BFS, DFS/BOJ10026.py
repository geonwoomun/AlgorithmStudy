# 백준 10026번 적록색약
# 그냥 일때와 적록색약일 때를 따로 만들어서 dfs로 풀었다.
import sys
sys.setrecursionlimit(1000000)
from sys import stdin
input = stdin.readline

N = int(input())

color = [list(input().rstrip()) for i in range(N)]
mx = (0,0,-1,1)
my = (-1,1,0,0)

gr = ('R', 'G')
b = ('B')

def grDfs(i,j):
    checkgr = gr if color[i][j] in gr else b
    check[i][j] = 0
    for k in range(4):
        x = i + mx[k]
        y = j + my[k]
        if(0<=x <N and 0 <= y < N and color[x][y] in checkgr and check[x][y] == 1):
            grDfs(x,y)

def dfs(i,j):
    std = color[i][j]
    check[i][j] = 0
    for k in range(4):
        x = i + mx[k]
        y = j + my[k]
        if(0<=x <N and 0 <= y < N and color[x][y] == std and check[x][y] == 1):
            dfs(x,y)
count = 0
grCount = 0
for k in range(2):
    check = [[1 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if(check[i][j] == 1):
                if(k==0):
                    dfs(i,j)
                    count +=1
                else:
                    grDfs(i,j)
                    grCount +=1

print(count, grCount)
