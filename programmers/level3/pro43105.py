# 프로그래머스 43105 정수삼각형

# 위에서부터 맨 밑에까지 갔을 때 가장 큰 숫자를 찾는 것.
# 근데 이거는 사실 위에서부터 하면 너무나 어려운거시고
# 밑에서부터 위로 가면 쉽게 풀 수 있따.
# 위로 갈 때 더한 것중 더 큰거를 덮어쓰는 식으로 하면 된다.
def solution(triangle):
    answer = 0
    for i in range(len(triangle)-1, -1, -1):
        for j in range(len(triangle[i])-1):
            triangle[i-1][j] = max(triangle[i][j] + triangle[i-1][j], triangle[i][j+1] + triangle[i-1][j])
    answer = triangle[0][0]
    return answer