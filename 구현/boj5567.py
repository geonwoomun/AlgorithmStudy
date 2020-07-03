from sys import stdin

input = stdin.readline

n = int(input())
m = int(input())

friends = {}
for i in range(1, n + 1):
    friends[i] = []

for j in range(m):
    f1, f2 = map(int, input().split())
    friends[f1].append(f2)
    friends[f2].append(f1)

friendsSet = set(friends[1])

for value in friendsSet:
    friendsSet = friendsSet | set(friends[value])

print(len(friendsSet) - 1)
