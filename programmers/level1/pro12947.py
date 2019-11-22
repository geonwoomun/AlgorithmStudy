# 프로그래머스 하샤드 수
# 좀더 개선해서 해봄
def solution(x):
    temp = str(x)
    temp2 = 0
    for i in range(len(temp)):
        temp2 += int(temp[i])
    if(x % temp2 == 0):
        return True

    return False