results = []
for i in range(10): # 19 x 19 의 배열이니깐 19개의 리스트를 받아서 2중 리스트로 만듦
    a= input().split()
    results.append(a)

x = 1  # 개미 시작 장소는 1,1임   (2,2라고 했지만 거기선 배열을 1,1부터 시작해서 난 0,0부터) 
y = 1
if(int(results[x][y]) == 2): # 만약 시작부터 먹이가 있으면 9로 바꾸고 바로 끝
    results[x][y] = 9
else :  # 아니면 시작부분을 9로 바꾸고 반복문 시작
    results[x][y] = 9
    while 1:
        if(int(results[x][y+1]) == 2):  # 오른쪽부터, 오른쪽 우선, 먹이가 있으면 9로 바꾸고 break
            results[x][y+1] = 9
            break
        elif(int(results[x][y+1]) == 0): # 오른쪽 갈 수 있으면 가고 9
            results[x][y+1] = 9
            y +=1
        elif(int(results[x+1][y]) ==2): # 밑에 먹이 있으면 밑으로 가고 9로 바꿈
            results[x+1][y] = 9
            break
        elif(int(results[x+1][y]) == 0): # 밑에 먹이 없으나 갈 수 있으면 가고 9로 바꿈
            results[x+1][y] = 9
            x+=1
        else: # 그 외의 경우에는 모두 break
            break

for a in results: # 값을 하나씩 출력함
    for b in a:
        print(b, end=" ")
    print(" ")