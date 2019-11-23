# 네트워크
# 아직 레벨3은 어려우니깐 다른 사람 코드를 보면서 공부를 해본다.
# 이해가 잘안됨...
# def solution(n, computers):
#     answer = 0
#     visited = [0 for i in range(n)] # 0으로 n크기만큼 초기화
#     def dfs(computers, visited, start): # dfs
#         stack = [start] # 시작부분이 들어있는 리스트
#         while stack: # 리스트가 빌때까지
#             j = stack.pop() # 리스트를 꺼낸다. pop 마지막것을 꺼냄.
#             if visited[j] == 0: # 그 꺼낸거의 visited가 0이면 즉 방문한게 아니면
#                 visited[j] = 1 # 방문을 했다고 바꿈.
#             for i in range(0, len(computers)): # 컴퓨터의 길이만큼 반복문..
#                 if computers[j][i] ==1 and visited[i] == 0: # j의 컴퓨터가 1이고 방문이 0이면
#                     stack.append(i) # 리스트에 추가..?
#     i=0
#     while 0 in visited: # visited의 모든 배열이 1이 될때까지 한다고한다..
#         if visited[i] ==0: # visited[i] 가 0이면
#             dfs(computers, visited, i) # dfs를 하고 답을 1 더한다.
#             answer +=1
#         i+=1
#     return answer

# 내가 다시 짜본 코드 dfs는 재귀가 더 쉬운것 같음.
def solution(n, computers):
    answer = 0
    visited = [0] * n
    def dfs(start):
        for i in range(n):
            if(start != i):
                if(computers[start][i] == 1 and visited[i] == 0):
                    visited[i] = 1
                    dfs(i)
    for i in range(len(computers)):
        if(visited[i] == 0):
            visited[i] = 1
            answer += 1
        else :
            continue
        for j in range(n):
            if(i != j and computers[i][j] == 1 and visited[j] == 0): # 1이고 연결되지 않은 녀석이면 
                visited[j] = 1 # 연결됐다고 하고
                dfs(j) # 그 다음으로 간다.  바로 dfs 함수를 해도 될 것 같지만 걸러서 넣기 위함..
    return answer

computers = [[1,1,0], [1,1,1], [0,1,1]]
n = 3
print(solution(n, computers))