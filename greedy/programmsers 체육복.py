def solution(n, lost, reserve):
    answer = n - len(lost)
    j = 0
    while(j < len(reserve)): 
        if(lost.count(reserve[j]) != 0) :
            answer += 1
            lost.remove(reserve[j])
            reserve.remove(reserve[j])
            continue;
        j +=1
           
    
    for value in reserve:
        if(lost.count(value-1) != 0) :
            lost.remove(value-1)
            answer +=1
        elif(lost.count(value+1) != 0):
            lost.remove(value+1)
            answer +=1
    
    return answer

# print(solution(7,[2,3,4],[1,2,3,6]))
print(solution(5,[1,2,3,5],[1,3,4,5]))