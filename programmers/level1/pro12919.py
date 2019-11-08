# 서울에서 김서방 찾기
def solution(seoul):
    for index,value in enumerate(seoul): # 배열의 index와 value 같이 접근하기 위한 내장함수 enumerate
        if(value == "Kim"):
            idx = index
    answer = "김서방은 " + str(idx) + "에 있다."
    return answer 

print(solution(["jane","Kim"]))