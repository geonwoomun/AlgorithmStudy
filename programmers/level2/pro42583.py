# 프로그래머스 다리를 지나는 트럭

# 내가 푼 방식은 진짜 막 짠거라서 효율성테스트가 있으면 바로 통과 못 할 것 같다.
# 하지만 효율성 테스트가 없었기에 정확성 테스트는 다 통과!
def solution(bridge_length, weight, truck_weights):
    answer = 0
    nowWeight = 0
    i = 0
    check = []
    count = 0
    while(1):
        if(i < len(truck_weights) and nowWeight + truck_weights[i] <= weight):
            nowWeight += truck_weights[i]
            check.append([truck_weights[i], 1])
            i += 1
        j = 0
        while(j < len(check)):
            if(check != []):
                check[j][1] += 1
                if(j == 0 and check[j][1] > bridge_length): # 제일 먼저 나가는 애는 맨 앞에 있는 애임. 다리의 길이를 지나면
                    nowWeight -= check.pop(0)[0] # 그래서 nowWeight에 그 트럭의 무게 만큼 빼주면서 check에서 뺐다.
                    count +=1 # 1개가 지났다고 세줌줌
                else :
                    j +=1
            
        answer +=1 # 한번마다 1초씩 더해줌.
        if(count == len(truck_weights)): # 끝까지 다 지나면 while문을 종료.
            break   
    return answer +1

bridge_length = 100
weight = 100
truck_weights = [10]*10

print(solution(bridge_length, weight, truck_weights))