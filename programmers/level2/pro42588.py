# 프로그래머스 탑

def solution(heights):
    answer = [0 for i in range(len(heights))]
    for i in range(len(heights)-1, 0, -1): # 마지막 부터 해서
        for j in range(i-1, -1, -1): # 그앞에껄로 차근차근 해서 
            if(heights[i] < heights[j]): # 더크면 answer에 그 값을 저장.
                answer[i] = j+1
                break
    return answer