# 프로그래머스 큰 수 만들기
# 테스트케이스 10번 시간초과 떄문에 고생 좀 했다.
# 10번은 99999999 일때의 예인것 같은데
# 그때는 내가 쓴 조건으로는 제거가 하나도 안되기 때문에
# 9의 숫자가 len 하고 같을 때는 k만큼 뺀 녀석의 number를 return 하도록했다.
# 아닐 경우에는 k가 0보다 클 때까지
# 앞의 숫자 보다 뒤의 숫자가 클 경우 앞의 숫자를 제거하는 식으로 하였다.
# 처음에는 "1234" 같은 것을 list로 바꾼다음에 비교하는 식으로 하였는데 이렇게하지 않고 그냥 string인 상태에서 비교가 가능하기 때문에
# 그렇게 했더니 훨씬 빨라졌다. 그리고 제거하는 것은 number[:i] + number[i+1:] 이런식으로하면 i 번째 글자를 뺀 합친 숫자가 된다. 
# 이 테크닉을 저번에 배운 이후로 더욱 유용하게 쓸 수 있게 된 것 같다.

def solution(number, k):
    i = 0
    if(number.count("9") == len(number)):
        number = number[:len(number)-k]
    else :
        while(k > 0):
            if(i > len(number) and k > 0):
                number = number[:len(number)-k]
                break
            if(i+1 < len(number) and number[i] != '9' and int(number[i]) < int(number[i+1])):
                number = number[:i] + number[i+1:]
                k -= 1
                if(i > 0):
                    i -= 1
            else :
                i += 1

    return number