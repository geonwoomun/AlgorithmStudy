## 3번 문제는 풀지 못했다.....
def solution(user_id, banned_id):
    answer = 1
    temp = []
    temp1 = []

    for value in banned_id:
        for value2 in user_id:
            if(len(value) == len(value2)):
                k = 0
                while(k < len(value)):
                    if(value[k] !='*'):
                        if(value[k] != value2[k]):
                            break
                    k +=1
                if(k == len(value)):
                    temp1.append(value2)
        temp.append(temp1)
        temp1 = []

    nanum = 1
    for i in range(0, len(temp)-1):
        for j in range(i+1, len(temp)):
            if(temp[i] == temp[j]):
                nanum *= 2*len(temp[i])

    for value in temp:
        answer *= len(value)
    answer /= nanum
    return int(answer)
