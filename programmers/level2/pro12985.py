# 프로그래머스 예상대진표

import math
def solution(n,a,b):
    answer = 1
    if (a > b): #크기에 따라 자리를 바꿔줌
        (a,b) = (b,a)
    while(1):
        if(a & 1 == 1 and a+1 == b): # a가 홀수이면서 a + 1 이 b랑 같을때
            break # 둘이 붙는 것이다!
        a = math.ceil(a / 2) # 아닐 경우 / 2를 한것을 올림 해준다. a가 3일 경우에 나누기 2를하고 올림을 하면 다음 경기에 2번으로 참가, 4일경우에도 2번
        b = math.ceil(b/2) # 둘다 같음.
        answer += 1 # 다음 라운드로 가는것.
    return answer

print(solution(8,2,3))