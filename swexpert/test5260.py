# 3일차 부분 집합의 합... 잘 모르겠습니다 . 10개중 8개 맞고 시간 초과.

T = int(input())
# 지금까지 다 더한거 + 다음것이  <= K
# if K - (prevSum + i) <= sums-i : # 지금까지 하고 남은 값이 남은 sums가 더 커야함.
#     subset(i+1, prevSum + i, sums-i)
# if K - prevSum <= sums:
#     subset(i+1, prevSum, sums-i)

# 아직 고려하지 않은 숫자 + 현재 숫자  >= K 해야함.
# 현재까지 더한거 + 다음 값이 > K 보다 크면 x
# 또는 현재 + 남은게 < W 보다 작으면 x
def subset(i, prevSum, sums):
    global N, K, answer
    if prevSum == K:
        answer +=1
        return
    if i == N+1 :
        return
    if prevSum > K :
        return
    if prevSum + sums < K :
        return                 
    
    subset(i+1, prevSum + i, sums-i)
    subset(i+1, prevSum, sums-i)

for t in range(1, T+1):
    N, K = map(int, input().split())
    answer = 0
    sums = 0
    for i in range(1, N + 1):
        sums += i
    subset(1, 0, sums)
    print("#", end='')
    print(t, answer)