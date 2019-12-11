# 백준 2455번 지능형 기차

from sys import stdin
input = stdin.readline

count = 0
maxCount = 0
for i in range(4):
    bye, hi = map(int, input().split())
    count -= bye
    count += hi
    maxCount = max(maxCount, count)

print(maxCount)