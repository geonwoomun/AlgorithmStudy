# 백준 1173 운동
# 문제 조건을 제대로 읽자!
# 맥박이하로 휴식하게 되면 최저맥박이 된다.
from sys import stdin
input = stdin.readline
N, m, M, T, R = map(int, input().split())
# 운동 N분 m 최저 맥박, M 최고 맥박 , T 운동할 때 올라가는 맥박, R 휴식할 때 내력나느 맥박


pulse = m
count = 0
exercise = 0
while exercise < N : # N번 만큼 하는데
    if pulse + T <= M: # 맥박이 운동을 해도 최고 이하이면
        pulse += T # 운동 ㄱㄱ
        count += 1 # 몇번했는지
        exercise +=1 # 운동 몇번했는지
    else :
        pulse -= R
        count +=1
        if pulse < m :
            pulse = m
    if pulse + T > M and pulse == m:
        count = -1
        break
print(count)