import math
#가장 먼저 실행되는 메인 코드
if __name__ == "__main__":
	# <---메인 코드의 시작---> 
	dotNum = int(input())
	dots = []
	dic = {}
	for i in range(dotNum):
		dots.append(list(map(int, input().split())))
	for i in range(len(dots)):
		for j in range(i, len(dots)):
			key = pow(dots[i][0] - dots[j][0], 2) + pow(dots[i][1] - dots[j][1], 2)
			if(dic.get(key) == None):
				dic[key] = 1
			else : 
				dic[key] +=1
	maxW = 0
	for value in dic.keys():
		if(dic[value] >= 4):
			if(maxW < value):
				maxW = value
				
	print("%0.2f" %float(maxW)) 