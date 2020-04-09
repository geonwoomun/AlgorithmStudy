# 프로그래머스 문자열 압축
# text 문자열 index 어디부터 count 몇개씩 now 몇번 같은지
def checkEqual(text, index, count, now): # 문자열에서 어디부터 몇개씩..
    if count + index>= len(text): # 마지막일경우
        return [now, text[index: index+count], index+count]

    if text[index:index+count] != text[index+count: 2* count + index]: # 다를 경우
        return [now, text[index:index+count], index+count] # 문자열반환, 
    
    now += 1
    [now, tempText, tempIndex] = checkEqual(text, count + index, count, now)
    return [now, tempText, tempIndex]

def solution(s):
    minLength = len(s)
    totalLength = len(s)
    
    for count in range(1, (len(s) // 2) + 1):
        resultText = ''
        index = 0
        while index <= len(s):
            now = 1
            if index + count >= len(s):
                resultText += s[index:]
                break
            [now, tempText, index] = checkEqual(s, index, count, now)
            if(now == 1):
                resultText += tempText
            else:
                resultText += (str(now) + tempText)
        if resultText != '':
            minLength = min(minLength, len(resultText))

    return minLength

s = "ababcdcdababcdcd"
print(solution(s))