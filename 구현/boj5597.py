from sys import stdin

input = stdin.readline

numbers = [0 for i in range(30)]

for i in range(28):
    numbers[int(input()) - 1] = 1

for index, value in enumerate(numbers):
    if value == 0:
        print(index + 1)

