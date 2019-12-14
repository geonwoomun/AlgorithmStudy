# 화물 도크

T = int(input())

for t in range(1, T+1):
    N = int(input())
    freight = [tuple(map(int,input().split())) for _ in range(N)]
    freight.sort(key=lambda x: (x[1],x[0]))
    time = 0
    count = 0
    for v in freight:
        if(v[0] >= time):
            count +=1
            time = v[1]
    
    print("#", end="")
    print(t, count)