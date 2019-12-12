# 백준 1057번 토너먼트
from sys import stdin
import math
input = stdin.readline

N, a, b = map(int, input().split())

if a > b:
    a, b = b, a
count = 1
while not(a & 1 == 1 and a + 1 == b):
    a = math.ceil(a/2)
    b = math.ceil(b/2)
    count +=1
print(count)