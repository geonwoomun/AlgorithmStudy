# BOJ 2437번 저울

# 할 수록 뭔가 블로그 내용들을 참고를 안 하면 잘 못 푸는 것 같아 우울하다.
# 아직 실력이 부족하다고 느낀다...
# 추들을 무게 순서대로 오름차순 정렬 한다음에 
# sumChu에 순서대로 더 하다가 그 다음 추가 sumChu + 1 보다 커버리면 sumChu + 1은 만들지 못하는 녀석이다.
# 1 1 2 6 을 하면 1과 2는 그냥 만들수 있는거고 1+1+2 가 4인데 5는 만들 수가 없게 되는 것이다. 그다음 오는게 6이니깐
# 6은 6으로 만들 수 있으니깐...sumChu가 4고 그다음이 +1을 한 5가 오거나 4가 와야 진행이 되는데 6이 와버리니 
# 안 되는...

N = int(input()) # 추들의 개수.

chus = list(map(int, input().split())) # 추들의 무게

def hamsu(chus): # 추들을 파라미터로 받아서 답을 리턴해줄 함수.
    chus.sort() # 무게순서대로 정렬
    sumChu = 0 # 무게들을 더할 변수
    for chu in chus: # chus 들의 요소들을 chu로 하나씩 받아서
        if(sumChu + 1 >= chu): # sumChu + 1 이 chu 보다 크거나 같아야 만들 수 있음.
            sumChu += chu # 그러면 chu를 더해서 하고
        else:
            return sumChu+1 # sumChu + 1 보다 chu가 더 큰 값이라면 sumChu + 1은 만들지 못하는 친구임. 최소니깐 바로 return
    return sumChu + 1 # for문을 다 돌았는데도 답이 return 이 안 됐다면 다 더한거 + 1이 만들지 못 하는 애 중 최소임.

print(hamsu(chus)) # 답을 출력