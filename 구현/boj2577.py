A = int(input())
B = int(input())
C = int(input())

result = list(map(int, str(A * B * C)))
arr = [0 for i in range(10)]

for i in result:
    arr[i] += 1

for count in arr:
    print(count)

