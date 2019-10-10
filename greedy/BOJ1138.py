# BOJ 1138번 한 줄로 서기

N = int(input())  # 몇 명을 입력 받을지


z = list(map(int,input().split()))  # 왼쪽에 몇명 있는지 센다.


result = []
for i in range(len(z)-1, -1, -1) : # 큰 사람부터 줄어가면서
    result.insert(z[i], N) # 그 인덱스에 N의 값을 넣는다. N값이 키와 같기 때문에.
    N -=1 # N의 값을 줄인다.

for value in result:
    print(value, end= ' ')