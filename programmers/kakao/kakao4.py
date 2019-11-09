# 4번은 문제 정확성은 다 맞추었는데 효율성 테스트에서 통과하지 못하였다.
# 효율성 테스트 1번까지만 어떻게 열심히해서 통과했는데 더 이상 통과할 수 없었다.
# python이라서 그런건가... c++로 해봐야하나라는 생각이 들기도 했고 
# 아니면 아직 효율적으로 짜는 방법을 잘 모르는건가..라는 생각도 했다.
def solution(k, room_number):
    answer = []
    temp = [0 for i in range(k)]
    length = len(room_number)
    append = answer.append
    index = temp.index
    for i in range(length):
        value = room_number[i]
        if(temp[value-1] < 1):
            append(value)
            temp[value-1] = 1
        else : 
            s = index(0, value)
            append(s + 1)
            temp[s] = 1

    return answer
