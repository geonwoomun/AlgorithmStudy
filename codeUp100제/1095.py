n = int(input())
a = input().split()
minNum = 24
for check in a:
    if(minNum > int(check)):
        minNum = int(check)

print(minNum)
