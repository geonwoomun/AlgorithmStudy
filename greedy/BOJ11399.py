N = int(input())

z = list(map(int,input().split()))

z.sort()
time = 0
temp = 0
for value in z:
    time += temp + value
    temp += value

print(time)