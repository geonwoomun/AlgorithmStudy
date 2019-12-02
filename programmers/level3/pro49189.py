# 프로그래머스 가장 먼 노드 
# 잘 모르겠어서 참고 했습니다..
# 새로운 것을 많이 배워갑니다.
# set 중복을 알아서 제거해주는 .. 방문 했는지 안 했는지 확인할 때 좋을 것 같습니다.
# defaultdict는 dictionary 자료형을 만들 때 기본 값을 설정해주는 것 같다.
from collections import deque, defaultdict

def bfs(start, tables, visited):
    q = deque()
    q.append((start, 0))
    numbers = defaultdict(lambda:0)
    visited.add(start)
    while q:
        node, cnt = q.popleft()
        for neighbor in tables[node]: # tables[node]에 있는걸 하나씩 꺼낸다.
            if neighbor not in visited: # 방문한적이 없으면 넣고 있으면 안 넣음. 왜냐하면 방문했었으면 그때가 제일 짧은 거리니깐.
                visited.add(neighbor) # 방문에 넣고
                numbers[cnt+1] += 1 # numbers[cnt + 1]에 개수를 하나씩 더함. 현재 거리 + 1이 몇개인지 센다.
                q.append((neighbor, cnt+1)) # 큐에 이웃과 cnt+1을 넣음. 그래야 현재 거리 + 1 한 걸로 나오기 때문에
    
    return numbers[cnt] # cnt가 최고 먼 애들의 거리와 같으므로 그것으 숫자를 리턴해주면 됨.

def solution(n, vertex):
    tables = defaultdict(set)
    for a,b in vertex : # vertex 하나씩 가져와서 a,b에 넣음.
        tables[a].add(b) # 기본 값이 set이라 tables[a] 하면 알아서 set으로 생기고 거기에 b를 추가 , a를 추가.
        tables[b].add(a)
    visited = set() # set이라서 방문을 한 것인지 아닌지 확인을 하기 좋음.
    return bfs(1, tables, visited)

n = 6
vertex = [[3,6],[4,3],[3,2],[1,3],[1,2],[2,4],[5,2]]
print(solution(n, vertex))