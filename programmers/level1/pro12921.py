## why 시간초과...
import math
def solution(n):
    arr = [i for i in range(n+1)]
    arr[0] = 0
    arr[1] = 0
    number = math.ceil(n / 2) # 2로 나눈것의 올림만큼의 개수로 시작. 왜냐하면 1은 소수가 아니고 2는 소수이다.
    # 그리고 나머지 짝수는 소수가 아니니깐 , 홀수 중에서 소수가 아닌 것들을 빼버릴 것임.
    for i in range(3, n+1, 2):
        if(arr[i] == 0): continue
        for j in range(3, int(math.sqrt(i))+1,2):
            if(i != j and i % j == 0):
                arr[i] = 0
                number -= 1
                break
    return number
print(solution(10000))