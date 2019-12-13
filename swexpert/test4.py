# 최소합
T = int(input())
test = 1

while test < T +1:
    N = int(input())

    temp = [list(map(int,input().split())) for i in range(N)]

    for i in range(N):
        for j in range(N):
            if(i == j == 0):
                continue
            if i > 0 and j > 0:
                temp[i][j] += min(temp[i][j-1], temp[i-1][j])
            elif i> 0:
                temp[i][j] += temp[i-1][j]
            else :
                temp[i][j] += temp[i][j-1]
    print("#",end="")
    print(test, temp[N-1][N-1])
    test +=1
