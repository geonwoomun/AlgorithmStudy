# 50, [1, 5, 10, 12, 22, 25], [1, 2, 3, 4]
# 3
# 이거일 때 안됨...
# 2020 카카오 블라인드 채용  외벽점검
def solution(n, weak, dist):
    dist.sort(reverse = True)
    minPeople = len(dist) # 최고 사람 수가 이거임.
    
    for i in range(len(weak)):
        people = 0
        temp = 0
        k = 0
        j = 0
        while(j < len(dist)):
            if(temp >= weak[k]):# temp는 현재 어디까지 했는지, weak[k] 보다 크면 그다음 weak까지 되는지 해보자.
                k +=1 # 그다음 weak로 가기 위해 1을 더함.
            else : # 그 다음으로.
                people +=1 # 1 더함.
                temp = weak[k] + dist[j] # weak[k]랑 dist 지금꺼랑 더해서 temp가 된다.
                k +=1
                j +=1
                if(temp >= weak[len(weak)-1]):
                    break
                
        if(minPeople > people):
            minPeople = people
        weak.append(weak[0] + n)
        weak.pop(0)
        
                
    return minPeople

n = 12
weak = [1,3,4,9,10]
dist = [3,5,7]
solution(n, weak, dist)