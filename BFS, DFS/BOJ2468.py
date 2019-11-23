# 안전영역
# DFS로 풀어보기
# 자바로 예전에 풀어봤었는데 요즘에 파이썬으로 공부하고 있으니깐 파이썬으로 다시 해본다.
# import sys
# sys.setrecursionlimit(100000) 을 하지 않으면 런타임에러가 뜸.
# 이거 때문에 뭐가 틀렸는지 계속 찾아 봤따... 계속 런타임에러가 뜨길래 ㅠㅠ
# 공식 도큐먼트에 의하면 해당 코드는 파이썬 인터프리터의 stack에
# 최대 깊이를 지정하는 것. 무한대의 recursion이 발생해서 overflow가 발생하는 것을 방지하기 위함.
# 이 문제에서는 그 만큼 깊이 있게 recursion으로 stack이 쌓이기 때문에 어느 정도가 진행되면 제한을 둬야한다..


import sys
sys.setrecursionlimit(100000)
N = int(input())

rain = [[]* N] * N
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
    rain[i] = rain[i] + temp

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


