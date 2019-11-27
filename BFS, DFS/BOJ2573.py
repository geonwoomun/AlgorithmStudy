# 백준 2573 빙산 
# 현재 pypy3로 밖에 안 됨...
import sys
from collections import deque # deque가 그냥 list 보다 빠르다.

n, m = map(int, sys.stdin.readline().split()) # sys로 입력 받는게 input()으로 입력 받는거 보다 빠르다.

bing = [list(map(int,sys.stdin.readline().split())) for _ in range(n)] 
cx = (0,0,1,-1) # 바뀌지 않는 값은 튜플이 list 보다 빠르다.
cy = (-1,1,0,0)

def bfs(i,j):
    q = deque()
    q.append((i,j))
    visit[i][j] = True
    while q :
        a, b = q.popleft()
        for k in range(4):
            x = a + cx[k]
            y = b + cy[k]
            if(x>=0 and x < n and y >= 0 and y < m and visit[x][y] == False): # 상하좌우가 밖으로 리스트 밖으로 나가지 않고 방문한게 아니면.
                if(bing[x][y] == 0): # 상하좌우중에 0인애가 있으면
                    if(bing[a][b] > 0): # 가운데 애가 0 보다 크면 -1 해줌줌
                        bing[a][b] -= 1
                else :
                    visit[x][y] = True
                    q.append((x,y)) 

count = 0 # 빙산이 다 녹을 때까지 몇 번
able = True # 가능한지 아닌지. bfs가 한번도 일어나지 않으면 다 0이라는 것. 즉 얼음이 다 녹았다는 것.
while(1):
    check = 0 # 빙산의 개수
    count += 1
    visit = [[False for _ in range(m)] for _ in range(n)] # 한번 할때 마다 초기화된 visit으로
    for i in range(n):
        for j in range(m):
            if(bing[i][j] > 0 and visit[i][j] == False):
                bfs(i,j)
                check +=1
                if(check > 1): # 2가 되면 바로 나오고 while까지 끝낸다.
                    break
    if(check > 1):
        break
    if(check == 0): # check 가 0 일때는 한번도 안 dfs가 안 일어났다는 것. 즉, 얼음이 다 녹은 것.
        able = False # count를 1으로 만들고 끝내고 count 를 출력.
        break

if able :
    print(count-1) # 처음 것은 0년째이므로 1빼서 답 출력.
else :
    print(0)



