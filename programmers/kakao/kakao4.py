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
