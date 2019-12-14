# 베이비 진 게임


T = int(input())

for t in range(1, T+1):

    card = list(map(int, input().split()))
    p1 = [0] * 10
    p2 = [0] * 10

    order = 1
    winner = 0
    for c in range(len(card)):
        if order == 1:
            p1[card[c]] +=1
            order +=1
            if(c > 4):
                for i in range(len(p1)):
                    if(i+2 < len(p1) and p1[i] >= 1 and p1[i+1]>=1 and p1[i+2] >= 1):
                        winner = 1
                        break
                    elif p1[i] == 3:
                        winner = 1
                        break            
        else:
            p2[card[c]] +=1
            order -=1
            if(c > 4):
                for i in range(len(p2)):
                    if(i+2 <len(p2) and p2[i] >= 1 and p2[i+1]>=1 and p2[i+2] >= 1):
                       winner = 2
                       break
                    elif p2[i] == 3:
                       winner = 2
                       break
        if winner :
            break  
    print("#", end="")
    print(t, winner)   