# 프로그래머스 H-Index
# 테스트케이스 9번에서 막혔다.
# [10,50,100]을 통과할 수 있도록 해야한다. 답이 3이 나와야한다.
# 다른 테스트 케이스는 while 문에서 다 완료된다.
# 10, 50 , 100 에서는 while문 안에서는 다 안되기 때문에 
# 마지막에 answer가 아직 0일 때 첫번째 원소값이 h 보다 크면 answer가 h가 되게 만들었떠니
# 테스트케이스 9번도 통과하면서 성공했다.
def solution(citations):
    answer = 0
    citations.sort()
    h = 1
    while(h < len(citations)):
        temp = len(citations) - h
        if(temp !=0 and citations[temp] >= h and citations[temp-1] <= h):
            answer = max(answer,h)
        h += 1
    if(answer == 0 and citations[0] >= h):
        answer = h
    return answer

citations = [10,50,100]
print(solution(citations))