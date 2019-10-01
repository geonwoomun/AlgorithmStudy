n = int(input())
a = []
results = [[0 for i in range(19)] for j in range(19)]
for i in range(n):
    b,c = map(int,input().split())
    results[b-1][c-1] = 1

for i in results:
    for j in i:
        print(j,end=' ')
    print('')