# 자연수 뒤집어 배열로 만들기
# ??? 내가 잘 못이해한건가 안풀리네

def solution(n):
    answer = str(n)
    answer = list(answer)
    answer = list(map(int, answer))
    answer.sort(reverse =True)
    return answer

print(solution(5890621521356))