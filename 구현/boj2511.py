from sys import stdin

input = stdin.readline

A = list(map(int, input().split()))
B = list(map(int, input().split()))

ascore = 0
bscore = 0
lastWinner = ""
for i in range(len(A)):
    if A[i] > B[i]:
        ascore += 3
        lastWinner = "A"
    elif A[i] < B[i]:
        bscore += 3
        lastWinner = "B"
    else:
        ascore += 1
        bscore += 1

print(ascore, end=" ")
print(bscore)

if ascore > bscore:
    print("A")
elif ascore < bscore:
    print("B")
elif lastWinner != "":
    print(lastWinner)
else:
    print("D")
