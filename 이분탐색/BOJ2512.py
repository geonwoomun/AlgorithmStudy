# 백준 2512 예산
# 프로그래머스에서도 있었던 문제라 쉽게 풀었다. 안 보고 풀어서 잘 복습이 된듯.
from sys import stdin
input = stdin.readline

N = int(input())
budgets = list(map(int, input().split()))
maxBudget = int(input())

answer = []

low = 0
high = max(budgets)

while low <= high:
    mid = (high + low) // 2
    result = 0
    for budget in budgets:
        if(mid > budget):
            result += budget
        else :
            result += mid
    if result > maxBudget:
        high = mid - 1
    else:
        low = mid + 1
        answer.append(mid)

print(max(answer))