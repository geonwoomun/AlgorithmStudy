# 프로그래머스 땅따먹기

# 1 2 3 5
# 5 6 7 8 
# 4 3 2 1 
# 이 있을 때 자기 자신과 같은 열은 더하지 못하므로
# 자기 자신의 열을 뺀 나머지 중 최대값을 밑으로 계속 더해줬다.
# 마지막 줄이의 max값을 출력하도록 하였다.
def solution(land):

    for i in range(1,len(land)):
        for j in range(len(land[0])):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])

    return max(land[len(land)-1])

land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))

