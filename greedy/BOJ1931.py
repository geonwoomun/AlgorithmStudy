# 백준 1931번 회의실배정 문제 

N = int(input()) # 회의 개수를 받는 변수

session = [] # 회의 시간들을 넣을 리스트

for i in range(0, N):  # N번 만큼 회의의 시작시간과 끝나는 시간을 받아 session list에 넣는다.
    session.append(input().split())

session.sort(key=lambda x: (int(x[1]), int(x[0]))) # session을 index 1을 기준으로 정렬하고 같을경우 index 0을 기준으로 정렬함.
last = 0 # 끝난 시간
count = 0 # 회의들의 개수
for value in session: # 정렬된 session을 하나씩 value로 받아서
    if(last <= int(value[0])): # value[0] 즉 시작시간이 끝난 시간보다 크거나 같을 때
        count +=1  # 개수를 1 더하고
        last = int(value[1]) #last를 현재 회의의 끝난 시간으로 바꾸어준다.

print(count)