from sys import stdin

input = stdin.readline

N, X = map(int, input().split())

A = list(map(int, input().split()))

for num in A:
    if X > num:
        if(num == A[-1]):
            print(num)
        else:
            print(num, end=" ")
