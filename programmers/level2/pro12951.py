# 프로그래머스 JadenCase 문자열 만들기
# 이 문제도 처음엔 리스트로 바꾸어서 풀려고 했는데 그냥 하는게 더 편한 것 같다.
# s라는 string 문자열 길이만큼 반복문을 도는데
# 공백일 경우에는 답에 공백을 더해주고 아닐 경우에 check가 true일 경우 대문자로해서 더하고
# check를 False로 바꾸고 check 가 false일 경우에는 소문자로 바꿔서 더해줬다.
# check는 공백이 나온 다음에는 True로 변경하게 해주어서 공백 나온 다음글자는 단어의 첫글자이므로
# 대문자로 되게 해주었다.
def solution(s):
    answer = ''
    check = True
    for i in range(len(s)):
        if(s[i] == " "):
            answer += " "
            check = True
        elif(check == True):
            answer += s[i].upper()
            check = False
        else:
            answer += s[i].lower()
    return answer


s = "3people unFollowed me"
print(solution(s))