# 첫 줄에 격자판의 세로(h), 가로(w) 가 공백을 두고 입력되고,
# 두 번째 줄에 놓을 수 있는 막대의 개수(n)
# 세 번째 줄부터 각 막대의 길이(l), 방향(d), 좌표(x, y)가 입력된다.

# 입력값의 정의역은 다음과 같다.

# 1 <= w, h <= 100
# 1 <= n <= 10
# d = 0 or 1
# 1 <= x <= 100-h
# 1 <= y <= 100-w

# 5 5   가로 세로
# 3      막대 개수
# 2 0 1 1   막대 길이 , 방향,  좌표 x,y
# 3 1 2 3   막대 길이 , 방향,  좌표 x,y
# 4 1 2 5   막대 길이 , 방향,  좌표 x,y

w, h = map(int, input().split())

results = [[0 for i in range(h)] for j in range(w)] # 0으로 h개수 만큼 채운 리스트를 w만큼 리스트로 만들어서 2중 리스트
n = int(input()) # 막대의 개수
for i in range(n): # 막대 개수 만큼 for문
    i, d, x, y = map(int, input().split()) # 길이, 방향, 좌표 x, y
    if(d == 0): # 가로면
        for a in range(i):
            results[x-1][y-1+a] = 1 # y좌표 하나씩 해서 1로 바꿈 그러면 가로줄이 1로 바뀜
    else: # 세로면
        for b in range(i):    
            results[x-1+b][y-1] = 1 # x좌표 하나씩 해서 1로 바꿈  그러면 세로가 1로 바뀜

for i in results:
    for j in i:
        print(j,end=' ')
    print('')
