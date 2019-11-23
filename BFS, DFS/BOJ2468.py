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

rain = [[]* N] * N # N * N 행렬을 만듦.
visit = [[1 for i in range(N)] for i in range(N)] # N * N 행렬에 방문 안했으면 1 방문 했으면 0으로 만들거임.

count = 0
height = 0
Max = 0

cx = [0,0,-1,1]    # X축 Y추으로 밑으로 위로 왼쪽으로 오른쪽으로를 뜻함.
cy = [1,-1,0,0]

def reset(N):    # 모두다 방문 안 한걸로 만들어주는 것.
    for i in range(N):
        for j in range(N):
            visit[i][j] = 1

def DFS(i, j, height): # DFS 할거임.
    if(i < 0 or i >= N or j < 0 or j >= N):  # N * N 행렬을 벗어나는 녀석이면 return
        return
    if(rain[i][j] > height) : # rain이 높이보다 크면 방문한걸로 바꿔줌.
        visit[i][j] = 0
    for m in range(4): # 위아래좌우를 확인 할 것임. dfs는 자식 우선이기 때문에. 점점 자식으로 가는
        a = i + cx[m]  # a를 현재 x + cx[0] , 1 2 3 순으로~
        b = j + cy[m] # b를 현재 y축 + cy[0] , 1, 2,3 순으로~~
        if(a >= 0 and a < N and b >= 0 and b < N and visit[a][b] == 1 and rain[a][b] > height ):
            DFS(a,b,height) # a랑 b가 행렬을 벗어나지 않고, 방문하지 않은 녀석이고, 높이보다 크면 dfs 함수를 재귀적으로 실행.

for i in range(N):
    temp = list(map(int, input().split())) # N만큼 rain의 높이를 받음.
    maxT = max(temp) # 그중에서 최고 높은 친구를 설정해봄.
    if(height < maxT):
        height = maxT
    rain[i] = rain[i] + temp # rain에 넣는다.

while(height >= 0): # height 마지막까지 해보고 max값을 구하여 반환.
    for i in range(N):
        for j in range(N):
            if(visit[i][j] == 1 and rain[i][j] > height): # 구역을 만들고 1 증가시킴.
                DFS(i, j, height)
                count += 1
    reset(N) # 반복문이 끝나면 height를 1을 줄였을 때를 다시 구해야하므로 reset 시킨다.
    if(count > Max) :
        Max = count
    count = 0 # 카운트도 0으로 만들고 height를 1줄인 값을 다시 max 값을 구해본다.
    height -= 1
print(Max)


