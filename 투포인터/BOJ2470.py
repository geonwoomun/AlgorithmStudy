from sys import stdin

input = stdin.readline

N = int(input())

yong = list(map(int, input().split()))
yong.sort()

start = 0
end = N - 1

a1 = 0
a2 = 0
minResult = 2000000000
while start < end:
    result = yong[start] + yong[end]
    if result == 0:
        print(yong[start], yong[end])
        break

    if abs(minResult) > abs(result):
        minResult = result
        a1 = yong[start]
        a2 = yong[end]

    if result > 0:
        end -= 1
    else:
        start += 1

print(a1, a2)
