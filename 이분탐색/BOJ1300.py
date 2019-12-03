# BOJ 1300 K번째 수
from sys import stdin

input = stdin.readline

N = int(input())
K = int(input())

low = 1
high = K  ## 하이를 K로 두고 하는거군... K번째수가 k보다 클리가 없으니 상한을 k로 잡고 고고
res = 0

while(low<=high):
    m = (low + high) // 2 
    cnt = 0 # cnt를 초기화 하고  cnt에는 m 보다 작은 녀석들의 개수를 담을꺼임. 작은 녀석들의 개수가 몇개인지.
    for i in range(1,N+1):  # N * N 배열을 만들었고 1부터 * N 까지, 
        cnt += min(m//i, N) # 최대 N개 까지고 m이 답일 때 i를 나눈거의 몫만큼 개수가 있다.
        # ex m = 4일때 1은 N이 3이면 3개까지 4보다 크거나 같으면 4개
        # 2일때는 1*2 , 2*2해서 2개
        # 3일때는 1*3 해서 1개 이런식...
    if(cnt < K): # 그래서 그 개수가 K보다 작으면 너무 m이 작다는 소리이므로 중간값을 올리기위해 low를 올림.
        low = m + 1 
    else :  # 아닐 땐 K와 같거나 cnt가 크다는 것이므로 high = m-1 해준다.
        res = m     # res를 저장해놓고 조건에 맞을때 끝나게 기다림.
        high = m - 1 

print(res)