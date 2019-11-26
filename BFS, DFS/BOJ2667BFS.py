# 백준 단지번호 붙이기 BFS로 풀어보기

N = int(input())

home = []
for i in range(N):
    home.append(list(map(int, input())))

cx = [0,0,1,-1]
cy = [1,-1,0,0]
count = 0

que = []
def bfs(i, j):
    que.append([i,j])
    while(que):
        a, b = que.pop(0)
        for k in range(4):
            x = a + cx[k]
            y = b + cy[k]
            if(x >= 0 and x < N and y >=0 and y < N and home[x][y] == 1):
                danji[-1] += 1
                home[x][y] = 0
                que.append([x,y])

danji = []

for i in range(N):
    for j in range(N):
        if(home[i][j] == 1):
            home[i][j] = 0
            danji.append(1)
            bfs(i,j)
            count += 1

print(count)
danji.sort()
for value in danji:
    print(value)