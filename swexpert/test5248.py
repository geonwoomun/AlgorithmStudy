# 5248 그룹 나누기

T = int(input())

def dfs(start) :
    visit.add(start)
    for v in dic[start]: # 인접한 애들을 친구한 애로 만들어줌.
        if v not in visit:
            dfs(v)

for t in range(1, T+1):
    N, M = map(int, input().split())
    dic = {}
    for i in range(N):
        dic[i+1] = []
    friend = list(map(int, input().split()))
    count = 0
    for i in range(0, len(friend)-1, 2):
        dic[friend[i]].append(friend[i+1])
        dic[friend[i+1]].append(friend[i])
    
    visit = set() # 이미 친구로 된 애인지 아닌지
    for i in range(1,N+1):
        if i not in visit: # 친구로 된 애가 아니면
            count +=1 # dfs 돌리면서 count 하나 늘림. 
            dfs(i)
    print("#", end='')
    print(t, count)