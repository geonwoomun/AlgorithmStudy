# BOJ 1946 신입사원
# 등수를 점수인줄 알고 있어서 오래 걸렸따.
# 문제를 잘봐야함..
# 코드를 잘 못 짠건지 파이썬이 느려서 그런건지... python3로 하면 시관초과가 뜨고 pypy3로 해야만 정답이 뜬다 ㅠㅠ

T = int(input())

for i in range(0, T):
    N = int(input())
    p = []
    for i in range(0, N):
        p.append(list(map(int,input().split())))
    
    p.sort(key= lambda x: x[0]) # 서류 성적을 기준으로 sort

    count = 1
    maxRank = p[0][1]  # 면접 성적 제일 높은 등수를 기록해놓고 그것 보다 낮으면 안되게 만든다. 서류 성적 기준으로 정렬되어 있으므로
                        # 면접성적까지 낮으면 둘다 낮은 것이기 때문.
    for value in p:
        if(maxRank > value[1]):
            maxRank = value[1]
            count += 1
    
        

    print(count)