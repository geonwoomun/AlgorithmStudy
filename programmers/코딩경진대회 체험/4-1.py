import math
dotNum = int(input())
dots = []
dic = {}
for i in range(dotNum):
	dots.append(list(map(int, input().split())))

maxS = 0
for i in range(len(dots)):
    for j in range(len(dots)):
        key = math.sqrt(pow(dots[i][0] - dots[j][0],2) + pow(dots[i][1] - dots[j][1],2))
        if(dic.get(key) == None):
            dic[key] =1
        else : 
            dic[key] +=1

    for k in dic.keys():
        if(dic[k] >= 2):
            temp = k
            for z in dic.keys():
                if(int(pow(z,2)) == int(pow(temp, 2) + pow(temp,2))):
                    if(maxS < temp*temp):
                        maxS = temp*temp
    dic.clear()

    

print("%0.2f"% float(maxS))