# 하샤드 수

def solution(x):
    answer = False

    temp = str(x)
    temp = list(temp)
    
    temp2 = 0
    for value in temp:
        temp2 += int(value)
    if(x % temp2 == 0):
        answer = True

    
    return answer