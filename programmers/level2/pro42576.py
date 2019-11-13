def solution(participant, completion):
    answer = ''
    temp = {}
    for name in participant:
        if(temp.get(name) != None):
            temp[name] += 1
        else : temp[name] = 0
    for name in completion:
        if(temp[name] == 0):
            temp.pop(name)
        else :
            temp[name] -= 1
    for i in temp.keys():
        answer = i
    return answer