# 백준 10816번 숫자카드2
import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
checkCards = list(map(int, sys.stdin.readline().split()))
cards.sort()
answer = [0 for _ in range(M)]

for i in range(M):
    right = N - 1
    left = 0
    while(left <= right):
        mid = (right + left) //2
        if(checkCards[i] == cards[mid]):
            answer[i] += 1
            left = mid + 1
        elif(checkCards[i] < cards[mid]):
            right = mid - 1
        else:
            left = mid + 1
for i in range(len(answer)): 
    if(i == len(answer) -1): # 마지막은 그냥 출력하고
        print(answer[i])
    else :
        print(answer[i], end=" ") # 마지막 아닐 땐 출력하고 한칸 뛰움.
