# 프로그래머스 자릿수 더하기

def solution(n):
    answer = 0

    while(n != 0):
        answer += n%10
        n = n//10
    return answer