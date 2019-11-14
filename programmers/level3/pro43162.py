# 네트워크
# 아직 레벨3은 어려우니깐 다른 사람 코드를 보면서 공부를 해본다.
# 이해가 잘안됨...
def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)] # 0으로 n크기만큼 초기화
    def dfs(computers, visited, start): # dfs
        stack = [start] # 시작부분이 들어있는 리스트
        while stack: # 리스트가 빌때까지
            j = stack.pop() # 리스트를 꺼낸다. pop 마지막것을 꺼냄.
            if visited[j] == 0: # 그 꺼낸거의 visited가 0이면 즉 방문한게 아니면
                visited[j] = 1 # 방문을 했다고 바꿈.
            for i in range(0, len(computers)): # 컴퓨터의 길이만큼 반복문..
                if computers[j][i] ==1 and visited[i] == 0: # j의 컴퓨터가 1이고 방문이 0이면
                    stack.append(i) # 리스트에 추가..?
    i=0
    while 0 in visited: # visited의 모든 배열이 1이 될때까지 한다고한다..
        if visited[i] ==0: # visited[i] 가 0이면
            dfs(computers, visited, i) # dfs를 하고 답을 1 더한다.
            answer +=1
        i+=1
    return answer
