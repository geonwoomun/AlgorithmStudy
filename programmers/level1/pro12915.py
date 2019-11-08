# 문자열 내 마음대로 정렬하기

def solution(strings, n):
    strings.sort(key = lambda s : (s[n:n+1], s))
    
    return strings

print(solution(["sun","bed","car"], 1))