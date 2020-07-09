from sys import stdin

input = stdin.readline

a, b = input().split()

minDiff = 50
for i in range(0, len(b) - len(a) + 1):
    diff = 0
    for j in range(len(a)):
        if a[j] != b[i + j]:
            diff += 1
    minDiff = min(minDiff, diff)

print(minDiff)

