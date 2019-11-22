# 프로그래머스 이중우선순위큐
# 이중 우선 순위 큐...
# 그럼 정렬을 한 녀석을 앞과 뒤에서 빼주면 된다.
# 그래서 제일 큰 값은 [-1]로 하고 작은 값은 [0]으로 했다.

def solution(operations):
    s = []
    for value in operations:
        v1 = value.split() # 빈칸을 기준으로 앞 뒤로 나눔.
        if(v1[0] == 'I'): # I 일 때 input
            if(v1[0] == "-"): 
                s.append(-int(v1[1][1:])) 
            else :
                s.append(int(v1[1]))
            s.sort()
        else :
            if(s != []): # 리스트가 빌 때는 pop이 안 되서 조건.
                if(v1[1] == '1'):
                    s.pop()
                else:
                    s.pop(0)
    if(s == []) : # 리스트가 비었으면 [0,0] 반환
        return [0,0]
    else : 
        return [s[-1], s[0]] # 아니면 [최댓값, 최솟값] 반환

operations = ["I 7", "I 5", "I -5", "D -1"]
print(solution(operations))