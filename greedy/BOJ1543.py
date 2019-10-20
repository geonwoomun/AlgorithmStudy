# BOJ 1543 문서검색
import sys       
p = list(sys.stdin.readline().strip()) # input으로 받아서 해도 되는데 sys.stdin.readline()이 더 빠르다해서 이걸로 했는데
r = list(sys.stdin.readline().strip()) # 백준 실행결과 시간은 같았다. strip으로 마지막 \n 개행 문자를 제거한다.
count = 0
i = 0
while (i < len(p) - len(r)+1): # i가 len(p) - len(r) +1 전까지만 하면 끝까지 검사한것과 같다고 할 수있따.
    check = True   
    for j in range(len(r)):
        if(p[i+j] != r[j]):
            check = False; # 중간에 다르면 false로 바꾼다.
            break;
    if(check): # 끝까지 검사 했을 때 트루이면 count를 늘리고 i를 len으로 바꾼다.
        count +=1
        i += len(r)
    else : # false일 경우 지금 i 보다 1 더한것부터 다시 검사
        i +=1

print(count)
