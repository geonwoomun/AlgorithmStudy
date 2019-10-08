## python3로 제출할 경우 시간초과,  pypy3로 제출할 시 정답.
N, K = map(int, input().split())  

z = []

for i in range(0, N):
    z.append(int(input()))

z.sort(reverse=True) # 역순으로 정렬해서
count = 0
for value in z:  # z에 있는 애들을 value로 하나씩 받아서
    if(value <= K): # 만약 value 보다 K가 크면 이제 최대한으로 넣을 수 있는 만큼 넣어야함
        i = 0             # i는 몇개를 넣을 수 있는지 쟤는 친구임.
        while 1:
            if(value * (i+1) <= K): # value에 i만큼 곱한 애가 K보다 작으면 아직 더 넣을 수 있는거임.
                i += 1
            else :   # 만약에 value가 더 크면 이제 못 넣는거임. i 값이 사용한 개수임
                count += i  # count에 i 값을 더 해줌.
                K -= value * i  # value를 빼 줌. 그래야 뒤에서 계산이 됨.
                break # while문을 빠져나옴.

print(count)