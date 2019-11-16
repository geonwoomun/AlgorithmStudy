# 프로그래머스 구명보트
# 탐욕법
# 잘 모르겠어서 다른 사람의 코드를 보았다.
def solution(people,limit):
    people.sort()
    length=len(people) # 길이만큼
    light=0
    heavy=length-1
    count=0
    while(light<heavy): # 헤비가 라이트보다 작을 때까지 반복
        if people[light]+people[heavy]<=limit: 
            count+=1
            light+=1
            heavy-=1
        else:
            heavy-=1
    return length-count

# 처음에 모두다 한명씩 탄다고 가정하고
# 라이트랑 헤비랑 탈 수 있으면 두명이서 탈 수 있으니깐
# count를 1 늘려서 length에서 빼면 2명이 같이 탄거처럼 계산된다.
# 제일 가벼운애랑 무거운애랑 해서 안 되면 무거운애를 줄이면 점차 탈 수 있게 된다.