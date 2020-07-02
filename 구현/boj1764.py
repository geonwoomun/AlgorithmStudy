N, M = map(int, input().split())

notListen = {}
notSee = {}
result = []
for i in range(N):
    notListen[input()] = 1

for j in range(M):
    now = input()
    if notListen.get(now, False):
        result.append(now)

print(len(result))
for res in sorted(result):
    print(res)
