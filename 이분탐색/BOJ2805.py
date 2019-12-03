# BOJ 2805 나무자르기
# python3로 제출하면 시간초과 나고 pypy3로 해야 통과. 블로그 찾아보니 다른 분들도 그런듯...

from sys import stdin
input = stdin.readline

N, M = map(int, input().split())

tree = list(map(int, input().split()))

l = 0
r = max(tree)
answer = 0

while(l <= r):
    mid = (l+r) // 2
    result = 0
    for namu in tree:
        if(namu > mid): # 나무를 잘랐을 때 0보다 클때만 빼줌.
            result += (namu - mid)
    if(result >= M): # 남은 나무가 들고가야할 나무 보다 많거나 같을 경우. 같을 때가 답일 경우가 큼!!.
        answer = max(answer, mid) # 답과 mid중에 큰 값을 answer에 넣음. 답이 커질 수록 남은 나무는 작아진다. 
        l = mid + 1 # mid 값을 크게 해줘서 result값을 더 작게 해주기 위함.
    else: 
        r = mid - 1

print(answer)