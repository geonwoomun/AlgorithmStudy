# 프로그래머스 카펫

def solution(brown, red):
    answer = []
    temp = brown + red # 전체 카펫의 수
    #가로길이는 세로 길이와 같거나, 세로길이보다 길다.
    garo = temp
    sero = 1
    
    while(garo >= sero):
        if((garo - 2 )* (sero -2) == red):
            answer = [garo, sero] # 제일 끝애 두개 뺀거를 곱했을 때 red랑 같아야함.
            break
        garo -=1
        sero = temp // garo
    return answer