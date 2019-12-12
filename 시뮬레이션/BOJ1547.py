# 백준 1547 공
from sys import stdin
input = stdin.readline

N = int(input())

ball = 1

for i in range(N):
    a, b = map(int, input().split())
    if(a == ball or b == ball):
        ball = a if not a == ball else b
print(ball)