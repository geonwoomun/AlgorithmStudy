# 프로그래머스 기지국 설치 
# 풀다가 50점 정도는 나오는데 더 이상 풀기 어려워서... 블로그 참고 했습니다.
# 좀 더 단순하고 효율적으로 생각하는 방법을 길러야겠다..

import math
def solution(n, stations, w):
    result = 0
    distance = []

    for i in range(1, len(stations)):
        distance.append((stations[i] -w -1) - (stations[i-1] +w))
    # 뒤의 기지국과 앞의 기지국 사이의 거리를 잰다. 

    distance.append(stations[0] - w -1) # 첫번째 기지국과 첫번째 아파트와의 거리
    distance.append(n - (stations[-1] +w)) # 마지막 기지국과 마지막 아파트와의 거리
    # 이렇게 하면 처음 기지국이 세워진 곳 빼고의 거리들을 모두 잴 수 있다.
    # w가 2 일 때 가운데 지을 경우 총 5개의 거리를 커버할 수 있다.
    # 거리가 6개 이상일 경우에는 기지국 1개를 더 지어야한다.

    width = 2* w + 1 # 주파수가 끼칠 수 있는 범위
    for dist in distance: # 거리들을 확인한다.
        if(dist == 0):  # 0이면 기지국 필요가 없으니 패스
            continue
        else :
            result += math.ceil(dist / width) # 위에 설명처럼 dist /width의 올림한 것 만큼 기지국이 필요하다.
    return result