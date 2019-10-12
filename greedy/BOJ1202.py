# BOJ 1202 보석도둑
# 이 문제를 통해 배운점이 많은 것 같다.
# 일단 import sys 하고 sys.stdin.readline()으로 input값을 받는 것이다. sys.stdin.readline() == input()
# 이라고 생각하면 될것 같다. 그런데 input()으로 받으면 시간초과가 뜨는데 sys로 받으면 시간초과가 안뜬다!!!
# 빠르게 받나 보다...
# 그리고 우선순위큐를 파이썬에서 사용해보았다. from queue import PriorityQueue를 통해서..

import sys
from queue import PriorityQueue

N, K = map(int, sys.stdin.readline().split()) # N 보석 개수 K 가방 개수

juwel = []
bag = []
for i in range(N):
    juwel.append(list(map(int,sys.stdin.readline().split())))

for i in range(K):
    bag.append(int(sys.stdin.readline()))

juwel.sort(key=lambda x:x[0]) # 보석 가치 높은 순으로 정렬해야 하는줄 알았는데 아니고 보석 무게가 작은 순으로 정렬해야했다.
bag.sort() # 가방은 적게 채울 수 있는거부터 한다.

que = PriorityQueue() # 우선순위 큐 선언.
w = 0
j = 0
for b in bag : 
    while(j < N and juwel[j][0] <= b):  # j는 index를 나타낸다. 보석이 무게순으로 되어있기 때문에 한번 계산한 보석은 뒤에서 또 쓸필요는 없다.
        # 보석의 개수인 N을 넘어가면 안된다. 그리고 가방의 무게가 보석 무게 보다 더큰거를
        que.put(-juwel[j][1]) # 우선순위 큐에 넣는다. 마이너스로 넣는 이유는 그래야 무게가 높은 애가 먼저 나오기 때문.. 우선순위큐가 값이 작은거부터 나와서 
        # 무게가 높은 애를 -를 주면 먼저 나오게 된다.
        j +=1  # 그리고 다음 보석도 진행. 가방 무게순이기 때문에 큐에 넣으면 뒤에 가방은 앞에꺼를 생각할 필요 없음. 왜냐하면 용량가 더크니 당연히 넣을 수 있기 때문에
    if(not que.empty()): # 지금 우선순위 큐에 들어 있는 애가 현재 가방이 담을 수 있는 녀석들임. 
        w += abs(que.get()) # 그래서 que.get()을 하면 제일 값이 작은 요소가 나오게 되는데 -를 붙인 제일 가치가 높은 보석이므로 abs를 통해 절대값으로 만들어 무게에 더해준다.
                            # que.get()을 하면 que에서 빠지면서 그 값이 return 된다.
print(w)