# 퀵정렬   인데 안 썼음..
T = int(input())

for t in range(1,T+1):
    N = int(input())
    element = list(map(int, input().split()))
    element.sort()
    print("#",end="")
    print(t, element[N//2])