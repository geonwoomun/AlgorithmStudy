import math
N = int(input())
check = 1
while check < N+1 :
    answer = ""
    a = float(input())
    count = 0
    i = 1
    while a != 0 and count <13:
        if a - math.pow(2,-i) >= 0:
            a -= math.pow(2,-i)
            answer += "1"
        else:
            answer +="0"
        i +=1
        count +=1
    if(count == 13):
        print("#", end='')
        print(check,"overflow")
    else:
        print("#", end='')
        print(check,answer)
    check +=1

