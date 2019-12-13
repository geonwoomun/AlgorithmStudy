dic = {
    "A" : 10,
    "B" : 11,
    "C" : 12,
    "D" : 13,
    "E" : 14,
    "F" : 15
}

T = int(input())
count = 1
while T > 0:
    s, temp = input().split()
    temp = list(temp)
    answer = ""
    for v in temp:
        if dic.get(v):
            answer += bin(dic.get(v))[2:].zfill(4)
        else:
            answer += bin(int(v))[2:].zfill(4)
    print(count, answer)
    count +=1
    T -= 1
            
