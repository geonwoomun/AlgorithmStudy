# 5번 문제도 테스트케이스는 다 통과했는데
# 효율성에서 통과하지 못하였다.
# 아직 거의다 2중 반복문으로 풀려고 해서 그러는 것 같다. 다른 스택 큐 같은것을 활용해서
# 잘 짜는법을 더 공부해보아야겠다.
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

