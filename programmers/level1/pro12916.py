def solution(s):
    temp = list(s);
    pNum = 0
    yNum = 0
    for value in temp:
        if(value.lower() == 'p'):
            pNum +=1
        elif(value.lower() == 'y'):
            yNum += 1
    
    if(pNum == 0 and yNum == 0):
        answer = True
    elif(pNum == yNum) :
        answer = True
    else :
        answer = False

    return answer