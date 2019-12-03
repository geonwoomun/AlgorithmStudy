# 백준 10816번 숫자카드2
# 이분탐색으로 분리 되어있는데 이분탐색 말고 다른 방법으로 풀었습니다.

import sys
from collections import defaultdict
N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
checkCards = list(map(int, sys.stdin.readline().split()))
cards.sort()
answer = [0 for _ in range(M)]
dic = defaultdict(lambda : 0) # defaultdict로 처음에 만들면 0으로 바로 만들어준다.

for i in cards: # dic에 cards가 있을 때마다 +1 해준다.
    dic[i] += 1

for i in range(M):
    if dic[checkCards[i]]: # 만약 dic에 체크하려는 카드가 있으면 
        answer[i] = dic[checkCards[i]] # 그 숫자를 answer에 넣어줌.
# 그러면 없는 애들은 0이 되고 있는 애들은 있는 숫자가 됨.

for i in range(len(answer)): 
    if(i == len(answer) -1): # 마지막은 그냥 출력하고
        print(answer[i])
    else :
        print(answer[i], end=" ") # 마지막 아닐 땐 출력하고 한칸 뛰움.
