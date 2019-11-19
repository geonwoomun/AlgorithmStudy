# 프로그래머스 숫자게임
# a랑 b를 각각 정렬을 한다음에
# B가 A보다 클 때 답을 하나 늘려가고 A와 B의 인덱스를 하나 늘리고
# B의 인덱스만 늘린다.
# A의 제일 작은 녀석 보다 큰 B 중에 제일 작은 요소가 매칭이 되게 하면된다.
# 탐욕적인...? 그런건듯
def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    i = 0 # B의 인덱스
    j = 0 # A의 인덱스
    while(i < len(A)):
        if(B[i] > A[j]):
            j +=1
            i +=1
            answer +=1
        else :
            i +=1

    return answer

A = [5,1,3,7]
B = [2,2,6,8]
print(solution(A,B))