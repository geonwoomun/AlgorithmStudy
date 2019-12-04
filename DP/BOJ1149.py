# BOJ 1149 RGB 거리

from sys import stdin
input = stdin.readline

N = int(input())
home = []

for _ in range(N):
    home.append(list(map(int, input().split())))

for i in range(1, N):
        home[i][0] += min(home[i-1][1], home[i-1][2])   # 3개만 있으니 가능함. 0은 1 ,2 를 더한 것 중 작은걸로
        home[i][1] += min(home[i-1][0], home[i-1][2]) # 1 은 0 2 를 더한 것중 작은걸로
        home[i][2] += min(home[i-1][0], home[i-1][1]) # 2 는 0 1 을 더한 것중 작은걸로, 그 전의 이웃한거랑 다른걸로 계속 칠해주면됨.

print(min(home[N-1]))

# 처음 푼 방식인데 좀더 복잡한거 같아.. 좀더 범용적??.. 이긴함 좀 덜 하드코딩이라 해야하나 하ㅏ..
# from sys import stdin
# input = stdin.readline

# N = int(input())
# home = []

# for _ in range(N):
#     home.append(list(map(int, input().split())))

# dp = [[0 for _ in range(3)] for _ in range(N)]

# dp[0][0] = home[0][0]   
# dp[0][1] = home[0][1]
# dp[0][2] = home[0][2]

# for i in range(1, N):
#     for j in range(3):
#         dp[i][j] = home[i][j] + min(dp[i-1][j+1 if j+1 < 3 else j+1 - 3 ], dp[i-1][j+2 if j+2 < 3 else j+2 - 3])

# print(min(dp[N-1]))