N, M = map(int,input().split())
A = list(map(int, input().split()))
right = 0
summary = 0
count = 0

for left in range(N):
    while summary < M and right < N:
        summary += A[right]
        right += 1
    if summary == M :
        count += 1
    summary -= A[left]

# while(left < len(A)):
#     if(result >= M):
#         result -= A[left]
#         left += 1
#     else:
#         if(right >= len(A)):
#             break
#         result += A[right] 
#         right += 1
#     if(result == M):
#         count += 1

print(count)