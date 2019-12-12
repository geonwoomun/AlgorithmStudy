# 백준 9517 아이 러브 크로아티아

from sys import stdin
input = stdin.readline
# 플레이어 8명 / 3분 30초가 지나면 폭탄 터짐.
# 정답을 못 맞추거나 스킵하면 다음 문제를 받음.
# 문제의 정답을 맞추면 다음 사람에게 넘김.
# 3분 30초는 210초임. 문제가 끝나도 다음에 못 넘기니깐 죽는듯.

K = int(input()) # 폭탄마
N = int(input()) # 질문 개수

allTime = 0
question = [input().split() for i in range(N)]
for time, check in question:
    time = int(time)
    allTime += time
    if allTime >= 210:
        break
    if check == "T":
        if K == 8 :
            K = 1
        else :
            K +=1

print(K)
