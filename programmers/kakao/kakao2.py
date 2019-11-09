import re
def solution(s):
    answer = []
    s = s.split("}")
    temp = []
    for i in range(len(s)):
        if(s[i] != ''):
            temp.append(re.findall('\d+',s[i]))

    temp.sort(key = lambda s : len(s))
    
    for s in temp:
        for value in s :
            if(answer.count(int(value)) == 0):
                answer.append(int(value))
                break;
    return answer

q = "{{4,2,3},{3},{2,3,4,1},{2,3}}"	;


solution(q)