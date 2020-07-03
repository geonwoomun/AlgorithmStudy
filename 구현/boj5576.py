w = [int(input()) for i in range(10)]
k = [int(input()) for i in range(10)]

w.sort(key=lambda x: -x)
k.sort(key=lambda x: -x)

print(sum(w[0:3]), sum(k[0:3]))
