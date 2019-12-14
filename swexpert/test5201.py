# 컨테이너 운반

# N 3 컨테이너수  M 2 트럭수
# N개의 화물의 무개
# M개의 트럭의 적재 용량


T = int(input())

for i in range(1,T+1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    container.sort(reverse=True)
    truck.sort(reverse=True)
    answer = 0
    j = 0
    for k in range(len(truck)):
        while j < N:
            if(truck[k] >= container[j]):
                answer += container[j]
                j+=1
                break
            j+=1
    print("#",end="")
    print(i, answer)

