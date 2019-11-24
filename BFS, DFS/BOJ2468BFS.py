# 안전영역
# BFS로 풀어보기

# 큐를 파이썬에선 리스트를 사용하여 append로 넣고 pop(0)으로 빼내면 구현 가능. stack 은 append로 넣고 pop()으로 빼내면 스택.
N = int(input())

rain = [[]* N] * N # N * N 행렬을 만듦.
visit = [[1 for i in range(N)] for i in range(N)] # N * N 행렬에 비에 모두다 잠겼다고 가정. 1 잠김, 0 안 잠김.

count = 0
height = 0
Max = 0
cx = [0,0,-1,1]    # X축 Y추으로 밑으로 위로 왼쪽으로 오른쪽으로를 뜻함.
cy = [1,-1,0,0]
Q = [] # BFS 함수 실행할 X,Y 좌표를 넣는 큐.
def reset(N):  # 모두다 방문 안 한걸로 만들어주는 것.
    for i in range(N):
        for j in range(N):
            visit[i][j] = 1

def BFS(i, j, height): # BFS 할거임.
    Q.append([i,j])  # BFS가 실행되면 일단 그것의 인덱스를 큐에 넣음.
    visit[i][j] = 0 # 사용했다는 표시
    while(Q != []): # 큐가 빌 때까지 계속 돌거임. 만약 상하좌우로 아무데도 갈수 없게 되면 큐가 비게 된다.
        a, b = Q.pop(0) # 큐에서 빼낸 값을 a,b에 넣고
        for m in range(4):
            x = a + cx[m]  # x를 현재 a + cx[0] , 1 2 3 순으로~
            y = b + cy[m] # y를 현재 b + cy[0] , 1, 2,3 순으로~~
            if(x >= 0 and x < N and y >= 0 and y < N and visit[x][y] == 1 and rain[x][y] > height ): # 조건에 모두 만족하면 이것도 큐에 넣는다.
                Q.append([x,y])
                visit[x][y] = 0

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
                BFS(i, j, height)
                count += 1
    reset(N) # 반복문이 끝나면 height를 1을 줄였을 때를 다시 구해야하므로 reset 시킨다.
    if(count > Max) :
        Max = count
    count = 0 # 카운트도 0으로 만들고 height를 1줄인 값을 다시 max 값을 구해본다.
    height -= 1
print(Max)
