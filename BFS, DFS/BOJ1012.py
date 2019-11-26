# 백준 유기농 배추
# 이 문제도
# import sys
# sys.setrecursionlimit(1000000)를 추가하지 않으면 런타임에러가 뜬다. 파이썬으로
# dfs를 풀 때는 꼭 필요한듯??
# N, M 순서를 반대로 주니깐 주의

import sys
sys.setrecursionlimit(1000000)
T = int(input())

while(T > 0):
    M, N, K = map(int, input().split())
    
    baechu = [[0]*M for i in range(N) ] # 배추가 심겨져있는지 체크크
    cx = [0,0,-1,1] # 상하좌우로 돌 수 있게 미리 설정해두는 값.
    cy = [1,-1,0,0]
    for i in range(K): # 배추가 있는 곳을 받아서 배추 값에 1을 넣어줌.
        a, b = map(int, input().split())
        baechu[b][a] = 1

    def dfs(i,j):
        baechu[i][j] = 0
        for k in range(4): # 상하좌우 하나씩.
            a = i + cx[k]
            b = j + cy[k]
            if(a >=0 and a < N and b >= 0 and b < M and baechu[a][b] == 1):
                dfs(a,b)
    answer = 0
    for i in range(N):
        for j in range(M):
            if(baechu[i][j] == 1) :
                dfs(i,j)  # 한 영역을 다ㅏㅏㅏ체크 할 수 있음. 한 영역 당 answer를 1씩 증가
                answer +=1
    T -=1
    print(answer)

# def dfs(i,j):
#     if(i<0 or i >= N or j <0 or j >= M): # 리스트 밖으로 나가면 끝냄
#         return
#     if(baechu[i][j] == 1): # 배추가 심어져있고 지렁이가 지나가지 않았으면
#         baechu[i][j] = 0
#         for k in range(4): # 상하좌우 하나씩.
#             a = i + cx[k]
#             b = j + cy[k]
#             dfs(a,b)