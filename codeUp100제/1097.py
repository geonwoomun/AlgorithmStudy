results = []
for i in range(19): # 19 x 19 의 배열이니깐 19개의 리스트를 받아서 2중 리스트로 만듦
    a= input().split()
    results.append(a)

n = int(input()) # 입력 받을 개수임

for i in range(n): # 개수 만큼 반복문을 돌림
    b,c = map(int,input().split())   # 값을 반대로 바꿀 x, y 좌표임
    for j in range(len(results)):  # 19번 돌려서 x 좌표들을 다 반대로 바꿈
        if(int(results[b-1][j]) == 0):
            results[b-1][j] = 1
        else:
            results[b-1][j] = 0   # j-1 == b 면 다 바꾼다  k-1 == c이면 다바꾼다.
    for k in range(len(results)): # 19번 돌려서 y좌표들을 다 반대로 바꿈.
        if(int(results[k][c-1]) == 0):
            results[k][c-1] = 1
        else:
            results[k][c-1] = 0
            
for a in results: # 값을 하나씩 출력함
    for b in a:
        print(b, end=" ")
    print(" ")