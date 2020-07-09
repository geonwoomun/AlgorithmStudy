from sys import stdin

input = stdin.readline

N = int(input())

yong = list(map(int, input().split()))

yong.sort()

i = 0
j = 1
k = N - 1

minResult = 3000000000
mini = 0
minj = 0
mink = 0

while i <= N - 3:
    j = i + 1
    k = N - 1
    # check = False
    while j < k:
        result = yong[i] + yong[j] + yong[k]
        # if result == 0:
        #     print(*[yong[i], yong[j], yong[k]])
        #     check = True
        #     break

        if abs(minResult) > abs(result):
            minResult = result
            mini = i
            minj = j
            mink = k
        if result > 0:
            k -= 1
        else:
            j += 1
    # if check:
    #     break
    i += 1

# if not check:
print(*[yong[mini], yong[minj], yong[mink]])

