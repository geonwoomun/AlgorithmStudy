# 프로그래머스 구명보트... 아직 못품
def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    
    i = 0
    while(i < len(people)):
        j = i + 1
        print(people)
        while(j < len(people)):
            if(limit >= people[i] + people[j]):
                people.pop(0)
                people.remove(people[j-1])
                answer += 1
                break
            j+=1
        if(people != []):
            people.pop(0)
            answer +=1
    return answer

people = [70,80,50]
limit = 100
solution(people,limit)