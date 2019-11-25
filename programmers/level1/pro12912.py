# 프로그래머스 두 정수 사이의 합

def solution(a, b):
    answer = 0
    if(a > b): # a가 더크면 a,b를 바꿔줌
        a,b = b,a
    for i in range(a,b+1):
        answer += i
    return answer

print(solution(3,5))
