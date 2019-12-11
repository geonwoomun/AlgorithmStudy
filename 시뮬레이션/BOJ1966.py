# BOJ 1966번 프린터 큐
from sys import stdin
input = stdin.readline

T = int(input())

while T > 0 :
    N, M = map(int, input().split()) # N 개수 M 위치
    paper = list(map(int, input().split()))
    check = [i for i in range(N)]
    count = 0
    while 1:
        maxPaper = max(paper)
        temp = paper.pop(0)
        tempCheck = check.pop(0)
        if(tempCheck == M and maxPaper == temp):
            count +=1
            break
        elif maxPaper == temp:
            count +=1
        else:
            paper.append(temp)
            check.append(tempCheck)
    print(count)
    T -=1