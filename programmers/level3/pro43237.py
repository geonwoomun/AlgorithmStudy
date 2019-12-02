# 프로그래머스 예산
def solution(budgets, M):
    left = 0
    right = max(budgets)
    answer = [] # 답이 되는 녀석들을 넣어 놓을거임.
    while(right >= left):
        mid= (left+right) // 2
        result = 0
        for cost in budgets: # 중간 값이 더 크면 중간 cost를 더하고
            if mid > cost :
                result += cost
            else : # 중간보다 cost가 더크면 중간값을 더함.
                result += mid
        if result > M : # 결과에 따라 어떡할지 정함.
            right = mid - 1
        else :
            answer.append(mid)
            left = mid + 1
    return max(answer) # 그 중에서 가장 큰 녀석 

budgets = [120,110,140,150]
M = 485

print(solution(budgets, M))