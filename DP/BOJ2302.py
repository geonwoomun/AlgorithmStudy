# BOJ 2302 극장좌석

from sys import stdin
input = stdin.readline

N = int(input())
M = int(input())

vip = set()
for i in range(M):
    vip.add(int(input()))

dp = [1 for i in range(N+1)]

for i in range(2,N+1): # 극장좌석에 앉을 수 있는 가지의수가 피보나치처럼 커짐 1자리 일땐 1 2자리 일땐 2 3자리일 땐 3 4자리일땐 5 
    dp[i] = dp[i-1] + dp[i-2] #이걸 알아내는 것이 중요.

answer = 1
cnt = 0
for i in range(1,N+1):
    if(i not in vip and i !=N): # vip에 없으면서 끝이 아니면 cnt 를 1 늘려준다.
        cnt += 1
    elif(i in vip): # 지금이 vip석이면 이제 여기 앞까지만 자리 바꿀 수 있는 친구들이니.
        answer *= dp[cnt] # 답에 지금까지 센 cnt의 dp 값을 곱하고 cnt 를 0으로 만들어줌.
        cnt = 0
    elif(i == N): # 끝이면 cnt+ 1 하면서 바로 곱해준다.
        cnt += 1
        answer *= dp[cnt]

print(answer)
