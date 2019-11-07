# 같은 숫자는 싫어

def solution(arr):
    answer = []
    answer.append(arr[0])
    for value in arr:
        if(answer[len(answer)-1] != value):
            answer.append(value)
   
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    
    return answer