n = int(input())
a = input().split()
b = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for check in a:
    b[int(check)-1] += 1

for value in b:
    print(value, end=' ')
