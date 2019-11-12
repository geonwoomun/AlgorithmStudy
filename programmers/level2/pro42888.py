# 2019 카카오 블라인드 채용 오픈채팅방.
# 레벨2
def solution(record):
    answer = []
    dic = {}
    for value in record: # 레코드에 있는 애의 마지막에 나온 아이디의 닉네임이 적용되므로
        # 딕셔너리를 사용해서 계속 덮어쓰기 했다. 
        s = value.split()
        if(s[0] != 'Leave'):
            dic[s[1]] = s[2]
        
    for value in record: # 레코드를 다시 읽어서 Enter면 dic의 value값님이 들어왔습니다.
        # Leave면 dic의 value 값님이 나갔습니다를 answer에 추가해준다.
        s = value.split()
        if(s[0] == 'Enter'):
            answer.append(dic[s[1]]+"님이 들어왔습니다.")
        elif(s[0] == 'Leave'):
            answer.append(dic[s[1]]+"님이 나갔습니다.")
    return answer

print(solution())