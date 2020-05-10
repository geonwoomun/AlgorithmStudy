N = int(input())

A = list(map(int, input().split()))

tempArr = [0]
summary = 0
for data in A:
    summary += data
    tempArr.append(summary)

M = int(input())

for i in range(M):
    x, y = map(int, input().split())
    print(tempArr[y] - tempArr[x-1])
