# 2019 카카오 개발자 겨울 인턴십 2번 튜플
def solution(s):
    answer = []
    tuples = []
    element = []
    temp = ''
    for index in range(0,len(s)):
        if (isNumber(s[index])):
            temp += s[index]
        elif (s[index] == ',' or s[index] == '}'):
            if (temp != ''):
                element.append(int(temp))
                temp = ''
        if (s[index] == '{' or index == len(s) -1):
            if (len(element) > 0):
                tuples.append(element)
                arr = []

    tuples.sort(key = lambda x : len(x))
    for items in tuples:
        for item in items:
            if item not in answer:
                answer.append(item)
        
    return answer

def isNumber(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")