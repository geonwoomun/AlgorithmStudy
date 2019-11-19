# 프로그래머스 최고의 집합
# n으로 나눈 몫을 답에 넣고 s를 뺀다
# n = 2, s = 9 로 예를 들면
# 9//2  = 4가 되고 4를 답에 넣고
# 9-4 를하면 5가 된다
# 이제 5//1 = 5이므로 답에 넣고 끝난다.

def solution(n, s):
    answer = []
    if(n > s ) :
        return [-1]
    for i in range(n, 0, -1):
        temp = s // i
        answer.append(temp)
        s -= temp
    return answer
