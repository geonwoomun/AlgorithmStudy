# 프로그래머스 더 맵게 
# heapq로 안 푸니깐 효율성에서 좋게 뜨지 않았음...

import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # scoville를 heap스럽게 만든다.
    while(scoville != []): # 리스트가 비지 않았을 때.
        if(len(scoville) == 1): # 길이가 1개 밖에 없으면
            if(scoville[0] < K):  # K 보다 작으면 못 하는거니간 -1 리턴
                return -1 
            else :  # 아니면 이때까지 한 answer를 리턴.
                return answer
        v1 = heapq.heappop(scoville) # heapq.heappop을 하면 제일 작은게 나옴.
        if(v1 >= K): # K 보다 제일 작은게 크면 답을 리턴
            return answer
        v2 = heapq.heappop(scoville) # 2번째 작은것.
        heapq.heappush(scoville, v1 + (v2 * 2)) # 공식대로 해서 힙에 다시 넣음.
        answer +=1 
        
    return answer