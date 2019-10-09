# BOJ 2217번 로프

N = int(input())

rope = []

for i in range(0, N):   # 하나씩 받음.
    rope.append(int(input())) 

rope.sort(reverse=True)  # 무거운 중량을 견딜 수 있는 로프부터 하기 위해서 무거운순서로 정렬
count = 0    # 로프의 개수를 세기 위한 것.
result = 0   # 결과 값을 담을 변수
for value in rope: # rope에 있는 것들을 value로 받아서
    count += 1 # count를 더 함
    if(result < value * count): # 현재 값에 총개수를 곱한 것이 result 보다 클 때 
        result = value * count # result 값을 바꿈.

print(result)