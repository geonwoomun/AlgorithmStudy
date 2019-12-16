# test 5209 최소 생산 비용
# DFS로 가다가 특정부분에 멈춰서 다시 하는게 백트래킹이였음!! 이미 어느정돈 알고 있었는데 오늘 다시 더 알게 된듯.


def DFS(start, price): 
    global best, N # 전역변수를 사용할 수 있게 해줌.
    
    if start == N: # 마지막 지역까지 왔을 때 
        best = min(best, price) # 최소값으로 설정해주고 끝낸다.
        return

    if price > best: # 중간에 가격이 더 커지면 그냥 더 체크할 필요없이 종료한다.
        return
    
    for i in range(N):
        if check[i] == False:
            check[i] = True  # 체크를 트루로 바꾸고 하다가
            DFS(start+1, price+elec[start][i]) # 검사가 끝나고 나서 다시 체크 False 한 상태로 새롭게 할 수 있또록 해줌.
            check[i] = False

T = int(input())

for t in range(1, T+1):
    N = int(input())

    elec = [list(map(int, input().split())) for _ in range(N)]
    best = 9999999
    check = [False] * N
    DFS(0, 0) # DFS함수를 실행.
    print("#", end='')
    print(t, best)