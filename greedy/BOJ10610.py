#BOJ 10610번 30

N = list(map(int,input()))  # int로 이루어진 list로 받았다.


N.sort(reverse=True) # 역순으로 정렬한다.
result = ''  # 나중에 값을 이어붙일 변수
if(sum(N) % 3 != 0 or N[len(N)-1] != 0):  # 30의 배수이려면 모든 숫자의 합이 3의 배수여야 되고 맨 마지막 수는 0이어야 한다.
    print(-1)
else:
    for i in N:
        result = result + str(i) # 위의 경우가 둘다 맞았을 경우에 각 값들을 result에 하나씩 붙여서 
    print(int(result))  # 정수로 출력한다.
    
    
