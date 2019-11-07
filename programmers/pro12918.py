# 문자열 다루기 기본 

def solution(s):
    answer = True
    temp = list(s)
    if(len(s) == 4 or len(s) == 6): # 문자열 길이를 검사하고
        for value in temp :    
            try:
                if(int(value)) : # value를 int로 바꾸는 것에서 에러가 나면
                    continue
            except : # 문자라는 뜻이기 때문에 answer를 False로 바꿈.
                answer = False
    else :  # 길이가 4 또는 6이 아니면 False로 바꿈.
        answer = False
         
    return answer
