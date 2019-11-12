# 카카오 2018 블라인드 채용 [1차] 다트 게임
# * 스타상. 당첨시 바로전에 얻은 점수 2배, # 아차상 해당 점수 0
def solution(dartResult):
    answer = 0
    temp = 0 # 이번 값
    temp2 = 0 # 전 값
    count = 0
    for i in range(len(dartResult)):
        print(dartResult[i])
        try:
            if(int(dartResult[i]) or int(dartResult[i]) == 0):
                if(count == 0):
                    answer += temp
                    temp2 = temp
                    temp = int(dartResult[i])
                    count +=1
                else : 
                    temp = int(str(temp) + dartResult[i])

        except :
            count = 0
            if(dartResult[i] == 'S'):
                temp = temp
            elif(dartResult[i] == 'D'):
                temp = temp*temp
            elif(dartResult[i] == 'T'):
                temp = temp*temp*temp
            elif(dartResult[i] == '*'):
                temp = temp *2
                answer += temp2
            elif(dartResult[i] == '#'):
                temp = -temp
        finally :
            if(i == len(dartResult) -1):
                answer += temp

    return answer

print(solution("1D2S#10S"))