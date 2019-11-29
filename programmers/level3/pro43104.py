# 프로그래머스 타일 장식물

def solution(N):
    element = [0 for i in range(N+1)] # 각 원소들을 저장할 리스트. 피보나치.
    element[1] = 1 # 처음에 1로 시작하니 넣어주고
    for i in range(2, N+1) : # 그 다음 부터는 i번째 요소는 i-1 번째 요소 + i-2번째 요소 이다.
        element[i] = element[i-1] + element[i-2]
    answer = (2*element[N] + element[N-1]) * 2 # 그래서 N번째 타일까지 쓴 전체의 둘레는 이 공식으로 된다. 두면은 N의 길이를 가지고 남은 2면은 N+ N-1 번째를 
    # 더한 길이를 가지므로 N 번째 + N번째 + N-1 번째를 *2를 해주면된다.
    return answer