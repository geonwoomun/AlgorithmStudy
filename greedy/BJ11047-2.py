## python3로 제출시 정답. 이게 더 효율적임!! 처음에 할 때 나누기를 생각을 못함. ㅠㅠㅠㅠ
N, K = map(int, input().split())   # N, K 를 받음

z = []  # 빈 리스트

for i in range(0, N): # N번만큼 동전을 입력 받음
    z.append(int(input()))

z.sort(reverse=True) ## 역정렬
count = 0 # 개수를 제출할 것
for value in z:  # z 리스트에서 하나씩 value로 받음.
    if(value <= K):  # value가 K 보다 작을 경우
        e = int(K / value) # 나눈 것의 정수 값을 count에 더하고 value 곱한 값을 K에 빼고.
        count += e
        K -= value * e
    

print(count)