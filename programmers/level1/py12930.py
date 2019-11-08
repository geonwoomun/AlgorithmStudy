# 이상한 문자 만들기

def solution(s):
    answer =''
    idx = 0 # s의 idx 하나씩 앞으로
    check = 0 # 해당 문자의 짝수번째인지 홀수번째인지 체크하는 수
    while(idx < len(s)): 
        if(s[idx] == ' '): 
            answer += s[idx]
            check = 0  # 공백이면 check를 0으로 만들고 idx는 하나 늘림
            idx +=1
        else :  # 공배아니면 짝수일 때 대문자로해서 추가하고 아닐때 소문자로해서 추가
            if(check % 2 == 0):
                answer += s[idx].upper()
                idx +=1
                check +=1
            else :
                answer += s[idx].lower()
                idx +=1
                check +=1
        
    return answer

print(solution("AA A"))