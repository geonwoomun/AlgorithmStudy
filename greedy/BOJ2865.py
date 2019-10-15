# BOJ 2865 나는 위대한 슈퍼스타 K

import sys

N, M, K = map(int,sys.stdin.readline().split()) # 참여자 수, 장르 수, 본선진출자

song = [] # 사람의 번호와 노래점수를 담을 리스트

for i in range(M):                                      
    song.extend(sys.stdin.readline().split()) # song에 한줄씩 추가를 한다.

result = [0] * N  # 참가자 수만큼 리스트를 만든다. 각 번호 -1의 인덱스에 자신의 최고점수를 넣는다.

for i in range(0, len(song)-1, 2): # 번호, 점수 순으로 리스트가 되어있기 때문에 i를 2씩 올리면 번호 점수 순으로 확인가능.
    if(float(song[i+1]) > result[int(song[i])-1]): # 자신의 최고 점수보다 현재 점수가 더 높으면 최고점수를 바꾼다.
        result[int(song[i])-1] = float(song[i+1])

SUM = 0
result.sort(reverse=True) # 점수가 높은 순서대로 정렬한다음
for j in range(0, K): # K 개만큼 더한다.
    SUM += result[j]
print(round(SUM,1)) # 첫째자리까지 반올림 한 값. 1째자리 까지 나오게 안 하니깐 틀렸었음.