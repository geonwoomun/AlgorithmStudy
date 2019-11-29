# 프로그래머스 숫자의 표현

def solution(n):
    answer = 1 # 자기 자신일 때 할 수 있으니 1개를 미리 세어둔다.

    for i in range(1,n):
        count = i # i 부터 시작해서 하나씩 더해가면서 같아지면 답을 더하고 넘어가면 그냥 끝낸다.
        for j in range(i+1, n):
            count += j
            if(count == n):
                answer +=1
                break
            elif(count > n):
                break
    return answer

print(solution(15))