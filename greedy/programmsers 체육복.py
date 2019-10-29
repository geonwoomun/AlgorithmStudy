def solution(n, lost, reserve): # 학생의 수, 잃어버린 학생들, 여분 체육복이 있는 학생들
    answer = n - len(lost)  # 체육복이 처음부터 있는 녀석들의 개수.
    j = 0
    while(j < len(reserve)):  # j가 reserve의 길이 보다 작을 때만.
        if(lost.count(reserve[j]) != 0) : # count가 인자값이 있는 개수를 세어준다. 즉 0이 나오면 없다는 뜻.
            answer += 1 # 그래서 답을 더해주고
            lost.remove(reserve[j]) # 잃어버렸지만 여분이 있는 녀석은 자기가 써야하므로 두군데서 다 빼준다.
            reserve.remove(reserve[j])
            continue; # 빼면 리스트기 때문에 앞으로 당겨져서 index가 바뀌기 때문에 j를 더해주지 않음.
        j +=1 # 아니면 j를 더해줌.
           
    
    for value in reserve: # 그래서 이제 reserve에 자신의 앞뒤 사람을 검사해서 있으면 하나씩 더해주고 잃어버린 녀석을 뺀다. 안빼면 중복 될수도 있기 때문에.
        if(lost.count(value-1) != 0) :
            lost.remove(value-1)
            answer +=1
        elif(lost.count(value+1) != 0):
            lost.remove(value+1)
            answer +=1
    
    return answer

# print(solution(7,[2,3,4],[1,2,3,6]))
# print(solution(5,[1,2,3,5],[1,3,4,5]))   몇가지 예외 테스트에 좋은 예