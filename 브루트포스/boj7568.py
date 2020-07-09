from sys import stdin

input = stdin.readline

N = int(input())

wh = []
for i in range(N):
    wh.append(list(map(int, input().split())))

rank = []
for i in range(N):
    nowRank = 1
    nowW, nowH = wh[i]
    for j in range(N):
        if i != j:
            compareW, compareH = wh[j]
            if nowH < compareH and nowW < compareW:
                nowRank += 1
    rank.append(nowRank)

print(*rank)
