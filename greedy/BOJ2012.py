# BOJ 2012번 등수 매기기
# 그냥 예상 순서대로 정렬한다음에 정렬한 인덱스를 실제 등수라 생각하고 예상 등수를 빼면 된다.
import sys

N = int(sys.stdin.readline())
D = []
for i in range(N):
    D.append(int(sys.stdin.readline()))

D.sort()

fire = 0
for a in range(0, len(D)):
    fire += abs(a+1 - D[a])

print(fire)