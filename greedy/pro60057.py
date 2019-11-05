# 프로그래머스 60057 / 2020 카카오 공채 문자열 압축.
# 모르겠습니다.
def solution (s) :
    temp = list(s)
    minResult = 9999
    for j in range(1, int((len(temp)/2)) + 1): 
        start = 0
        num = 1
        temp2 = ''
        for i in range(j, len(temp) + 1, j): 
            print(temp[start:i], temp[i: i+j])
            if(i < len(temp) and temp[start : j] == temp[j: 2* j]):
                num += 1
                start += j
            else :
                if(num == 1) :
                    temp2 += temp[start:j][0]
                else:
                    # temp2 += str(num) + temp[start:i][0]
                    temp2 += str(num) + ''.join(temp[start:j])
                num = 1
                start +=j
                print(temp2)
        minResult = min(minResult, len(temp2))

    print(minResult)
       


print(solution("aabbaccc")) # 2a2ba3c