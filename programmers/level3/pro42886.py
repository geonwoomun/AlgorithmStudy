# 프로그래머스 저울
# 제일 작은 애를 계속 더한 값 + 1 이 그 다음 값 보다 작으면 더한값 + 1 은 못 만드는 친구이다.
# 아니라면 다 더한 값 + 1 이 답
def solution(weight):
    weight.sort()
    temp = weight.pop(0)
    while(len(weight) != 0):
        v1 = weight.pop(0)
        if(temp + 1 < v1):
            return temp + 1 
        temp += v1
        
    return temp + 1
