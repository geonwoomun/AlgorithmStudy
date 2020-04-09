# 프로그래머스 Summer/Winter Coding(2019) 종이접기

def reverse(lists):
    return [bit ^ 1 for bit in lists[::-1]]

def solution(n):
    answer = [0]
    if (n > 1):
        for i in range(2, n + 1):
            answer = answer + [0] + reverse(answer)
    return answer
