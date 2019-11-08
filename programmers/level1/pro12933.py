# 정수 내림차순으로 배치하기

def solution(n):
    n = str(n)
    temp = list(n)
    temp.sort(reverse=True)
    answer = ''
    for value in temp:
        answer += str(value)
    return int(answer)