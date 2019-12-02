# 백준 10815번 숫자 카드  / 이분탐색
# 어려운 문제는 아니다.

import sys

N = int(sys.stdin.readline())
card = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
checkCard = list(map(int,sys.stdin.readline().split()))
answer = [0 for _ in range(len(checkCard))]
card.sort()

for i in range(len(checkCard)): # checkcard 하나씩 비교한느데 모든 card와 비교하는 것이 아닌 이분탐색으로 1/2씩 줄여가면서 해서 훨씬 빠르다.
    right = N - 1 
    left = 0
    while right >= left: # 가운데부터 시작해서 right >= left 일 때까지
        mid = (right + left) // 2
        if(checkCard[i] == card[mid]): # 같아지면 자기 자리의 answer에 1로 바꾸고 반복문 끝냄.
            answer[i] = 1
            break
        elif(checkCard[i] < card[mid]): # 아닐 경우 이분탐색이 되게 만들어준다.
            right = mid - 1
        else :
            left = mid + 1

for i in range(len(answer)): 
    if(i == len(answer) -1): # 마지막은 그냥 출력하고
        print(answer[i])
    else :
        print(answer[i], end=" ") # 마지막 아닐 땐 출력하고 한칸 뛰움.
