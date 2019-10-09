N = int(input())  ## 그리디 맞나? 일단 안한다

z = list(input())

count = 0

for i in range(0, N):
    if(i == 0) :
        z[i] = int(not bool(int(z[i])))
        z[i + 1] = int(not bool(int(z[i+1])))
    elif(i == N-1):
        z[i] = int(not bool(int(z[i])))
        z [i - 1] = int(not bool(int(z[i-1])))
    else:
        z[i] = int(not bool(int(z[i])))
        z [i - 1] = int(not bool(int(z[i-1])))
        z[i + 1] = int(not bool(int(z[i+1])))

print(z)