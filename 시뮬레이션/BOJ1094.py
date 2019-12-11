# BOJ 1094 막대기

from sys import stdin
input = stdin.readline

X = int(input())

S = 64
count = 0
dist = 0
while 1:
    if(dist + S > X):
        S = S//2
    else :
        dist += S
        count +=1
        if(dist == X):
            break

print(count)