# 프로그래머스 시저 암호.

def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if(s[i] == ' '):
            answer += " "
        else :
            temp = ord(s[i]) + n
            if(ord(s[i]) >= 97 and ord(s[i]) <= 122):
                if(temp > 122):
                    temp -= 26
            elif(ord(s[i]) >=65 and ord(s[i]) <= 90):
                if(temp > 90):
                    temp -= 26
            answer += chr(temp)
    return answer