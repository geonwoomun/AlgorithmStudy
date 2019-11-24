# 백준 유기농 배추 BFS로 풀어보기기
# BFS는 sys ~~ 필요없다 재귀가 아니라 그런듯.
# N, M 순서를 반대로 주니깐 주의

T = int(input())

while(T > 0):
    answer = 0
    M, N, K = map(int, input().split())
    baechu = [[0]*M for i in range(N) ] # 배추가 심겨져있는지 체크크
    cx = [0,0,-1,1] # 상하좌우로 돌 수 있게 미리 설정해두는 값.
    cy = [1,-1,0,0]
    for i in range(K): # 배추가 있는 곳을 받아서 배추 값에 1을 넣어줌.
        a, b = map(int, input().split())
        baechu[b][a] = 1
    Q = [] # 한 배추당 4번 돌릴거니깐 한개씩 넣어준다.
    def BFS(j, k):
        Q.append([j,k]) # Q에 x y좌표로 만든 리스트를 넣음
        baechu[j][k] = 0 
        while(Q != []):
            a, b = Q.pop(0) # Q에서 나온 것을 순서대로 하나씩 대입.
            for k in range(4): # 상하좌우 하나씩.
                x = a + cx[k] # 위에 만들어둔 상하좌우 도는 것을 한다음에
                y = b + cy[k]
                if(x >= 0 and x < N and y >= 0 and y < M and baechu[x][y] == 1): # 리스트 밖으로 안 튀어나가고 1이면 0으로 만들고 Q에 그 좌표를 넣는다.
                    baechu[x][y] = 0 # 상하좌우 다하고 나면 또 그다음 녀석의 상하좌우 그다음 녀석의 상하좌우... 순서로로
                    Q.append([x,y])

    for j in range(N):
        for k in range(M):
            if(baechu[j][k] == 1):
                BFS(j,k);
                answer += 1
  
    T -=1
    print(answer)