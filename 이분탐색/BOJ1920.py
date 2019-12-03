# BOJ 1920 수 찾기

from sys import stdin
input = stdin.readline

N = int(input())
num = list(map(int,input().split()))

M = int(input())
checkNum = list(map(int,input().split()))

num.sort()

for i in checkNum:
    left = 0
    right = N-1
    check = False
    while left <= right :
        mid = (left + right) // 2
        if(i == num[mid]):
            check = True
            break
        elif(i < num[mid]):
            right = mid -1
        else : 
            left = mid + 1
    if(check == True):
        print(1)
    else:
        print(0)
