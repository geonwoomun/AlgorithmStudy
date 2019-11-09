# 카카오 겨울인턴쉽 코딩테스트
# 이렇게 짜는게 아닐거 같지만... 내 생각나는 대로 짰는데 다 통과했다.
# 이것도 또한 제대로 푸는 방법이 아닐거 같기애 효율성은 좋지 못할 것 같다.
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