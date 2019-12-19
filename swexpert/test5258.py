# 해피 박스   0/1 배낭 문제랑 같음.
T = int(input())

for t in range(1,T+1):
    N, M = map(int, input().split()) # N 배낭 최대 무게, M 개수
    box = [tuple(map(int, input().split())) for i in range(M)]
    box.sort(key = lambda x:((x[1] / x[0]), -x[0]), reverse=True)
    m = [[0 for i in range(N+1)]for i in range(len(box) + 1)] # 메모 하기 위한 것 .   m[box개수][최고무게] 만큼 만듦.
    for i in range(1, len(box)+1):   # m[i][j] 에는 i번째 박스, j무게 까지 계산 했을 때의 최고 가치가 들어있음.
        for j in range(1, N+1):   # 최고 박스 무게,   1 부터 N(최대)까지
            if box[i-1][0] > j : # 박스 무게가  > j 현재 박스무게 보다 크면 그 전 박스 값. 현재 박스는 넣을 수가 없으니깐.
                m[i][j] = m[i-1][j] 
            else : 
                m[i][j] = max(m[i-1][j], m[i-1][j-box[i-1][0]] + box[i-1][1]) 
                                # 이전 값과 ,   현재 배낭 무게 만큼 뺀 무게에서 이전의 최고 가치  + 현재 무게 중 최대값.
                
    print("#", end='')
    print(t, m[len(box)][N]) # 이제 마지막엔 최고의 가치가 담겨져 있음.