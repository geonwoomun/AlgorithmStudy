## why 시간초과...
import math

def solution(n):
    arr = [i for i in range(n+1)]
    arr[0] = 0
    arr[1] = 0
    if(n > 3):
        for i in range(4, n+1, 2):
            arr[i] = 0
    for i in range(3, int(math.sqrt(n))+1, 2):
        if(arr[i] == 0): continue
        for j in range(3, n+1,2):
            if(arr[i] != arr[j] and arr[j] % arr[i] == 0):
                arr[j] = 0
    num = 1       
    for i in range(3, n+1,2):
        if(arr[i] !=0):
            num +=1
    return num

print(solution(10))