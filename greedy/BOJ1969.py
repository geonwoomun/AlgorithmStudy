#BOJ 1969 DNA

# N DNA 수 M 문자열의 길이
N, M = map(int, input().split()) # N, M 을 정수형으로 받는다.
z = []  # DNA들을 받을 리스트
for i in range(0, N):
    z.append(list(input())) # DNA 수 만큼 z에 추가해서 받는다.

count = 0 # Hamming Distance를 셀 변수
result = '' # Hamming Distance를 최소로 만드는 DNA s를 저장할 변수

# 내가 할거는 N개의 DNA를 같은 index를 다 검사해서 하나씩 넘어가는거임..
# 그러니까 모든 DNA의 0번째 인덱스 검사~ 1번째 인덱스 검사~ 2번째 인덱스 검사~ 이런식..
for i in range(0, M): # M개의 글자씩 있으니깐 
    s = [] # A, C, G, T의 값들을 넣을 리스트 , 각각은 index 마다 0으로 초기화해서 새로 수를 셈
    A = 0
    C = 0
    G = 0
    T = 0
    for j in range(0, N): # 돌아가는 DNA들
        if(z[j][i] == 'A'): # j DNA의 i index가 'A'이면 A값 1 더하고 C면 C값 1 더하고 ...
            A +=1
        elif(z[j][i] == 'C'):
            C +=1
        elif(z[j][i] == 'G'):
            G +=1
        elif(z[j][i] == 'T'):
            T +=1
    s.append(A)
    s.append(C)
    s.append(G)
    s.append(T) # 다 s 리스트에 넣어서
    if(max(s) == A): # 최대값에 따라서 result에 더하고 count에 다른 수를 다 더해서 넣음. 그래야 result 값과
                    # 다른거의 수 즉 Hamming Distance가 더해지는 것임. 그 Hamming Distance들을 다 더한 것이 답.
        result += 'A'
        count += C+G+T
    elif(max(s) == C):
        result += 'C'
        count += A+G+T
    elif(max(s) == G):
        result += 'G'
        count += A+C+T
    elif(max(s) == T):
        result += 'T'
        count += A+C+G
print(result)
print(count)