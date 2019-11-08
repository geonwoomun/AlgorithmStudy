# 19 카카오 블라인드 채용 / 실패율
def solution(N, stages):
    answer = []
    arr = []
    stages.sort()
    num = 1
    while(N + 1 != num):
        temp = stages.count(num)
        if(temp == 0):
            arr.append([num, 0])
        else : 
            arr.append([num, temp/len(stages)])
            while(temp != 0):
                stages.pop(0)
                temp -=1
        num +=1
    arr.sort(key = lambda s : (s[1], -s[0]), reverse=True)
    
    for value in arr:
        answer.append(value[0])
    return answer

