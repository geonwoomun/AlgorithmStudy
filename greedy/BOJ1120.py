#BOJ 1120번 문자열
# A와 B의 길이가 다르니깐 A를 유동적으로 이동해보며 비교해봐야함
# A[0]이 B[0]부터 시작할 때 B[1]부터 시작할때 .... 등등
# 어차피 앞이나 뒤에 아무 알파벳이나 추가 가능하다고 했으니 같은 알파벳을 추가한다는거임.
# 그니까 [0]부터 시작하면 뒤에 같은 알파벳 추가하는거고 [1] [2].. 부터 시작하면 앞과 뒤 또는 앞에
# 같은 알파벳을 추가하는 느낌으로~~ 
# 그래서 비교 했을때 최대한 적게 차이나는 count수를 답으로 제출.

a, b = map(str, input().split()) #두개의 문자열들을 받는다
a = list(a)
b = list(b)

ans = 999999  # 최소값
for i in range(0, len(b)-len(a)+1): # 앞에서 부터 차근차근 비교할거임. A랑 B의 길이가 다르니(A가 짧거나 둘이 같음)  
    count = 0
    for j in range(0, len(a)):
        if(a[j] != b[j+i]):  # 다르면 COUNT를 늘림
            count +=1
    ans = min(ans, count) # 최소값을 정답으로 함.

print(ans)
