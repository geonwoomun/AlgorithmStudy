N = int(input())

su = list(map(int, input().split()))

su.sort()
print(su[len(su) // 2 - 1])

