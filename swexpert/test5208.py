# 전기버스2
# 재귀적으로 생각하는게 어려운듯...ㅠㅠ
def DFS(i, count):
    global result, end

    if i >= end:  # 끝까지 왔을 때
        if result > count: # reulst가 count 보다 크면 result = count가 된다. 
            result = count
        return
    if result < count: # count가 result 보다 크면 그건 필요 없는 녀석.
        return
    
    start = i
    life = test[i]
    for j in range(start+life, start, -1): # start + life 부터 start까지 -1 씩 줄여가면서
        DFS(j, count+1) # DFS를 돌려~  재귀적으로 계속 돌려짐.
T = int(input())

for t in range(1, T+1):
    test = list(map(int, input().split()))
    count = 0
    result = 99999999
    end = test[0]
    DFS(1, count)
    print("#",end='')
    print(t, result-1)