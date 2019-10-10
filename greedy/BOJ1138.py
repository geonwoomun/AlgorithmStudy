# BOJ 1138번 한 줄로 서기
# 신기하게 끝에서부터 차근차근 새 배열에 넣으면 된다!
# insert를 사용하면 index에 해당 값을 넣을 수 있는데
# insert가 그 자리에 들어가면서 그 자리에 값을 삭제하지 않고 그 자리부터 그 뒷자리 값들을 한칸씩
# 밀어내기 때문에 가능한 것 같다.
# 예를 들어 5 0 0 2 1 0 으로 받으면
# 끝에서부터 시작하며 6을 0에 넣는다 [6]
# 5를 1에 넣는다. [6,5]
# 4를 2에 넣는다. [6,5,4]
# 3을 0에 넣는다. [3,6,5,4]
# 2를 0에 넣는다. [2,3,6,5,4]
# 1을 5에 넣는다. [2,3,6,5,4,1] 이 된다.
# 내가 원하던 결과랑 같아지게 된다.  

N = int(input())  # 몇 명을 입력 받을지


z = list(map(int,input().split()))  # 왼쪽에 몇명 있는지 센다.


result = []
for i in range(len(z)-1, -1, -1) : # 큰 사람부터 줄어가면서
    result.insert(z[i], N) # 그 인덱스에 N의 값을 넣는다. N값이 키와 같기 때문에.
    N -=1 # N의 값을 줄인다.

for value in result: # 하나씩 출력.
    print(value, end= ' ')