# 코딩경진대회 체험 2번

N, M = map(int, input().split())
temp = [[i, 0] for i in range(1, N+1)]
for i in range(M):
	a, b = map(int, input().split())
	if( a == b or a < 1 or a> N or b < 1 or b > N):
		continue
	temp[a-1][1] += 5
	temp[b-1][1] += 3
		
temp.sort(key=lambda x:x[1], reverse = True)
Rank = 0
count = 1
tempS = 0
for value in temp:
	if(value[1] != tempS):
		Rank += count
		count = 1
	else : 
		count +=1
	print(Rank, value[0], value[1])
	tempS = value[1]