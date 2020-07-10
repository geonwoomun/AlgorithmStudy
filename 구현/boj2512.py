N = int(input())

E = list(map(int, input().split()))

M = int(input())

maxE = max(E)

minE = 0
result = 0
while minE <= maxE:
    mid = (minE + maxE) // 2
    temp = 0
    for value in E:
        if value > mid:
            temp += mid
        else:
            temp += value
    if M >= temp:
        minE = mid + 1
        result = max(result, mid)
    else:
        maxE = mid - 1

print(result)
