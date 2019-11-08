# 나누어 떨어지는 숫자배열

def solution(arr, divisor):
    answer = []

    for value in arr:
        if(value % divisor == 0):
            answer.append(value)
    answer.sort()
    if(answer == []):
        answer.append(-1)
    return answer