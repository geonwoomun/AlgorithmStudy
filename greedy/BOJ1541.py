# BOJ 1541 잃어버린 괄호

# - 기준으로 자르고 + 녀석들을 다 더한 다음에 빼기를 진행하면 최소가 된다.
import sys
S = list(sys.stdin.readline().strip().split('-')) # -를 기준으로 자른다.
# 그러면 55-50+40 기준으로 55, 55+40 으로 나뉜다.
result = []   
for value in S:
    if(value.find('+') != -1): # 만약에 +를 포함하고 있다면, 포함하고 있으면 위치가 나오고 아니면 -1
        temp = list(map(int,value.split('+'))) # +를 기준으로 자른거를 temp에 넣은다음
        result.append(sum(temp)) # result에 그 합을 넣는다.
    else :
        result.append(int(value)) # 문자열로 저장되어 있기 때문에 int형으로 바꿔준다.

ans = result[0] # 처음 값을 ans에 넣고... ans은 답을 출력할 녀석.

for i in range(1,len(result)): # 1부터 result의 끝까지 뺀다. -를 기준으로 나눈 것이니깐.
    ans -= result[i]

print(ans)