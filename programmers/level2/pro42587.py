# 프로그래머스 프린터

def solution(priorities, location):
    answer = 0
    temp = []
    for i in range(len(priorities)):
        temp.append([i, priorities[i]]) # 인덱스와 우선순위를 넣음.
    while(1):
        v1 = temp[0][1]
        check = True
        for i in range(1,len(temp)):
            if(temp[i][1] > v1): # 우선 순위가 제일 높은지 체크 아니면 False로 바꿈.
                check = False
                break
        if(check == True and temp[0][0] == location): # 우선 순위가 제일 높고 찾는 것이면
            return answer + 1 # 답을 반환
        elif(check == True): # 우선순위만 제일 높으면 빼내고 출력한 횟수를 더함..
            temp.pop(0)
            answer += 1
        else: # 우선순위가 높은 것이 아니면 빼서 다시 넣음.
            temp.append(temp.pop(0))
    return answer