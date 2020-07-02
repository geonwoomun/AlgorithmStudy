N = int(input())

Box = 0

while True:
    if N % 5 == 0:
        Box += N // 5
        print(Box)
        break
    N -= 3
    if N < 0:
        print(-1)
        break
    Box += 1

