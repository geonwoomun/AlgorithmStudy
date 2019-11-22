# 프로그래머스 야근 지수
# 리스트로 하고, Priority que를 사용해도 시간 초과가 뜨길래 heapq로 만들어서 하였음.
# heapq로 만들어서 heappop을 하면 가장 작은 값을 반환해주기 때문에 
# 처음에 heap으로 만들 list를 - 값으로 다 바꿔준 다음에 heap으로 만들고
# 넣을 땐 다시 -v1이런식으로 넣어서 제대로 작동하게 만들었음.


import heapq

def solution(n, works):
    answer = 0
    i = 0
    for i in range(len(works)):
        works[i] = -works[i]
    heapq.heapify(works)
    while(n > 0):
        v1 = -heapq.heappop(works)
        if(v1 > 0):
            v1 -= 1
        heapq.heappush(works, -v1)
        n -= 1
    
    for i in range(len(works)):
        w = -works[i]
        answer += w*w
    return answer

works = [4,3,3]
n = 4

print(solution(n, works))