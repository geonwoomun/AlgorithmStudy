# 백준 5532번 방학숙제
from sys import stdin
input = stdin.readline

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())


while A > 0 or B > 0:
    A -= C
    B -= D
    L -=1

print(L)

