# 프로그래머스 레벨2 위장

# dic라는 딕셔너리 안에 옷들의 개수를 셀 것이다.
# 파이썬에서는 딕셔너리를 사용해서 해시를 구현할 수 있다.
# 옷들은 같은 것이 없다고 했기 때문에 종류가 같으면 1개씩 더해줬다.
# 그 옷의 종류가 처음 들어오는 것이면 입지 않았을 때와 입었을 때를 해서 2를 넣어줬다.
# 그 옷의 종류를 다 곱하면 모든 경우의 수가 나온다.
# 그리고 아무것도 안 입는 경우는 없기 때문에 1을 빼준다.

def solution(clothes):
    answer = 1
    dic = {}
    for cloth in clothes:
        if(dic.get(cloth[1]) == None):
            dic[cloth[1]] = 2 
        else : 
            dic[cloth[1]] += 1
    for key in dic.keys():
        answer *= dic[key]
    answer -= 1
    return answer

max()