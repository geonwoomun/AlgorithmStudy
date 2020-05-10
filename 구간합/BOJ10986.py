N, M = map(int, input().split())

arr = list(map(int, input().split()))

summary = 0
number = [0]
for data in arr:
    summary += data
    number.append(summary)

count = 0
for i in range(M):
    count += number[i] * (number[i] -1) // 2
print(count)