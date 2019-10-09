# BOJ 5585번 거스름돈

changes = int(input())  # 돈을 받는다.

changes = 1000 - changes  # 1000원에서 돈을 빼서 잔돈으로 만든다
coins = [500, 100, 50, 10, 5, 1]  # 가지고 있는 동전. 큰거부터 순서대로 계산하게 한다.
count = 0
for coin in coins:  
    if(changes != 0): # 남은 잔돈을 다 거슬러준게 아닐 때.
        if(coin <= changes):  # 현재 coin이 changes 보다 작거나 같을때
            num = int(changes / coin)  # 나눠서 최대한의 개수 만큼.. 빼내고 count 수를 늘리고 changes를 줄인다.
            count += num  
            changes -= num*coin

print(count)

