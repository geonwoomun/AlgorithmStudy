# 프로그래머스 줄 서는 방법
import math

def solution(n, k):
    answer = []
    numberList = [i for i in range(1, n+1)]
    while (n != 0):
        temp = math.factorial(n) // n # 한개에 몇개씩의 값이 있을지 알 수 잇음.
        index = k // temp
        k = k % temp
        if k == 0:
            answer.append(numberList.pop(index-1))
        else :
             answer.append(numberList.pop(index))
        n -= 1
    
    return answer

print(solution(3,5))

# 3 2 1  // 3  2개씩 있다.    4 // temp  => 몫 2. 나머지 0   
# 3 2 1 //3 => 2 -> 1개당 2개씩 경우의 수가 있다. k 5니깐 2개하면 2개는 넘어가고 1남음. 2개 넘어갔으니 다음꺼 넣고
# 1가지고 다음꺼 ㄱㄱ  2 1/ 2  temp = 2  index 1 // 2  index = 0  k 1 // 2 1 