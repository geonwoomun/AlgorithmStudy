import math
N = int(input())
if(N == 1): 
    print(0)
else:
    sosu = [True for i in range(0, N+1)]
    sosu[0] = False
    sosu[1] = False
    Number = []
    for i in range(2, N + 1):
        if(sosu[i] == True):
            Number.append(i)
            for j in range(i*i, N+1, i):
                sosu[j] = False
    # def Eratosthenes(n): 
    #     Primes=[] 
    #     isPrime=[1 for i in range(n+1)] 
    #     isPrime[0]=0 
    #     isPrime[1]=0 
    #     for i in range(2, n+1): 
    #         if isPrime[i]==1: 
    #             Primes.append(i) 
    #             for j in range(i*i, n+1, i): 
    #                 isPrime[j]=0 
    #     return Primes
    # sosu = Eratosthenes(N)
    left = 0
    right = 0
    count = 0
    result = 0
    while(left < len(Number)):
        if(result >= N):
            result -= Number[left]
            left += 1
        else:
            if(right >= len(Number)): break
            result += Number[right]
            right += 1
        if(result == N):
            count += 1
    print(count)


