# BOJ 8980 택배

## 사람들 블로그 보고 풀어도 뭔지 잘 모르겠어서.... 3~4시간 만에 일단 포기...

N, C = map(int, input().split()) # N 마을 수, C 트럭의 용량

M = int(input()) # 보내는 박스 정보의 개수 M

z = [] # 박스 정보를 담을 리스트

for i in range(0, M):
    z.append(list(map(int,input().split())))

z.sort(key=lambda x: (x[1],x[0]))

# 0 번째 보내는 마을 2번째 받는 마을. 3번째 량.  
# 그럼 이제 실어서 그 마을에서 내리고. 다시 실고 ...
NowBox = 0
totalBox = 0
s = []
for vil in range(1, N+1): # 마을 ...
    if(s != []):
        for value in s:
            if(value[1] == vil):
                NowBox -= value[2]
                totalBox += value[2]
    for zValue in z: # z 에 든 정보를 도는것..
        if(NowBox < C):
            if(zValue[2] <= C - NowBox): # 만약 도착지이고, 택배양이 실을 수 있는 양ㅂ다 작으면
                NowBox += zValue[2] # 현재에 실고..
                # totalBox += z[i][2] # 그것의 토탈 박스를 적고...
                s.append(zValue) # s에 추가하고
                z.remove(zValue)
            elif(zValue[2] > C- NowBox): # 만약 도착지이고 내가 실을게 더 많으면
                zValue[2] = C-NowBox
                # totalBox += z[i][2]
                NowBox += zValue[2]
                s.append(zValue)
                z.remove(zValue)

print(totalBox)

