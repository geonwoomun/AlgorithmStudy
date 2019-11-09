def solution(stones, k):
    answer = 0
    while(1):
        temp = k
        lenth = len(stones)
        for i in range(lenth):
            if(stones[i] > 0):
                stones[i] -= 1
                temp = k
            else :
                temp -=1
                if(temp < 1):
                    return answer
        answer +=1
        
    return answer

