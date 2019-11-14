# 안전영역
# DFS로 풀어보기
# 자바로 예전에 풀어봤었는데 요즘에 파이썬으로 공부하고 있으니깐 파이썬으로 다시 해본다.


N = int(input())

rain = []
visit = [[1 for i in range(N)] for i in range(N)]

count = 0
height = 0
Max = 0

cx = [0,0,-1,1]
cy = [1,-1,0,0]

def reset(N):
    for i in range(N):
        for j in range(N):
            visit[i][j] = 1

def DFS(i, j, height):
    if(i < 0 or i >= N or j < 0 or j >= N): 
        return
    if(rain[i][j] > height) :
        visit[i][j] = 0
    for m in range(4):
        a = i + cx[m]
        b = j + cy[m]
        if(a >= 0 and a < N and b >= 0 and b < N and visit[a][b] == 1 and rain[a][b] > height ):
            DFS(a,b,height)

for i in range(N):
    temp = list(map(int, input().split()))
    maxT = max(temp)
    if(height < maxT):
        height = maxT
    rain.append(temp)

while(height >= 0):
    for i in range(N):
        for j in range(N):
            if(visit[i][j] == 1 and rain[i][j] > height):
                DFS(i, j, height)
                count += 1
    reset(N)
    if(count > Max) :
        Max = count
    count = 0
    height -= 1
print(Max)

