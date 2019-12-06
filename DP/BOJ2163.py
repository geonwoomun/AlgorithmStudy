# 2136 초콜릿 자르기
# 왜 dp인줄은 잘 모르겠지만..
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())

print((N-1) + (N *(M-1)))  # 열심히 규칙 찾아보니 이 규칙이라 해서 맞았는데 거의다 n*m-1해서 푼듯?