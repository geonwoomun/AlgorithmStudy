#BOJ 1654번 랜선자르기
from sys import stdin
input = stdin.readline

K, N = map(int, input().split())

lan = []
for i in range(K):
    lan.append(int(input()))
low = 0
high = max(lan)
answer = 1
while(low <= high):
    mid = (high + low) // 2
    result = 0
    if mid == 0 : # 이 녀석 때문에 계속 런타임에러 뜸..  high low가 둘다 0이라 mid가 0 이되면 ... 1cm간격으로 잘라야된다는 뜻.
        break
    for d in lan:
        result += d // mid
        if result >= N:
            answer = max(answer, mid)
            break
    if(result < N):
        high = mid - 1
    else :
        low = mid + 1

print(answer)