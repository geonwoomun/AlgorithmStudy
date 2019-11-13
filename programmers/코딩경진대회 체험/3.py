# 코딩경진대회 체험 3번. 색종이
# 백준에도 있는 문제더라..
# 처음에 잘 모르겠어서 답을 찾아보았다.
# 나는 너무 열심히 접근했다고 해야하나... 좀 단순하게 생각하지 못했던것 같다.
# 답에 거의 3중~ 4중 반복문인데 이건 아니라 생각하며 접근했기 때문에 좀...
# 근데 문제 풀이에 이렇게 되어있더라.
# 답은 100 x 100으로 되어있는 리스트에 덮어지면 1씩 더해줘서 1이상인 녀석들의
# 개수를 반환하는 것이었다.
testNum = int(input())

while(testNum > 0):
	paper = int(input())
	answer = 0
	allPaper = [[0 for i in range(100)] for i in range(100)]
	paperDot = []
	for i in range(paper):
		paperDot.append(list(map(int,input().split())))
	
	for value in paperDot:
		for i in range(10):
			for j in range(10):
				allPaper[value[0]+i][value[1]+j] += 1
	
	for value1 in allPaper:
		for value2 in value1:
			if(value2 >= 1):
				answer +=1
	print(answer)
	testNum -= 1