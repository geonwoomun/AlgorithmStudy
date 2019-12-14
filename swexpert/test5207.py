# 이진 탐색 오타하나 때문에 한참을 잡아먹음..
T = int(input())

for t in range(1, T+1):
    Alen, Blen = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    count = 0
    for value in B:
        left = 0
        right = Alen-1
        direct = 0
        while left <= right:
            mid = (left+right) // 2
            if value == A[mid]:
                count +=1
                break
            elif value > A[mid]:
                left = mid + 1
                if direct == -1:
                    break
                direct = -1
            else :
                right = mid - 1
                if direct ==  1:
                    break
                direct = 1
                
    print("#", end="")
    print(t, count)