# 프로그래머스 섬 연결하기
# 잘 모르겠어서 여러가지 찾아봤다... 그런데 어려운것들이 많앗는데 그중에 쉬운걸로 찾아서
# 디버그 해보며 이해했음..!

def solution(n, costs):
    answer = 0
    check = [0 for _ in range(n)] # n의 숫자만큼 다 0으로 만듦. 0은 연결이 안되었다. 1은 연결 된 것.
    costs.sort(key=lambda x:x[2]) # 거리 오름차순으로 정렬을 한다. 제일 거리가 짧게 만들 것이기 때문에.
    check[costs[0][0]] = 1 # 제일 짧은 것부터 시작 할 것이기 때문에 이렇게 설정 해줌.
    while(sum(check) != n): # 모든 check가 1이 되면 sum이 n과 같아짐. 즉 모두다 방문하면.
        for value in costs: # costs를 value로 꺼내서
            if(check[value[0]] or check[value[1]]):
                if(check[value[0]] and check[value[1]]): # 둘다 이미 방문한 것이면 할 필요 없다.
                    continue
                else : # 둘중에 하나만 연결 되어있을 때만.. 
                    answer += value[2] # 답을 더하고
                    check[value[0]] = 1 # 둘다 방문한걸로 바꾸어줌. 어느게 방문했던것인지 모르기 때문에 걍 둘다 해줌.
                    check[value[1]] = 1 
                    break # 브레이크하고 처음부터 다시해야 앞에서 건너뛴거 체크가능함.
                          # 이번에 연결을 함으로서 한개가 연결 돼서 다른것들이 연결 될 수 있기 때문에...?
    return answer

n = 4
costs = [[0,1,1], [2,3,2],[0,2,4]] # 이렇게 하면 0 1 연결 되고 2 3 연결 될거 같지만 2 3 은 하나도 연결이 되어있지 않기 때문에 0 1, 0 2, 2,3 순서로 연결 된다.
print(solution(n, costs))