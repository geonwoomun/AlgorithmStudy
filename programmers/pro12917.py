# 문자열 내림차순으로 배치하기

def solution(s):
    temp = list(s)
    temp.sort(reverse=True)
    answer = ''
    for value in temp:
        answer += value


    return answer

print(solution("Zbcdefg"))