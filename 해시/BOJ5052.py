t = int(input())

while t > 0:
    n = int(input())
    number = []
    for i in range(n):
        number.append(input())
    
    number.sort()
    
    result = True
    for i in range(1,len(number)):
        length = len(number[i-1])
        if number[i][:length] == number[i-1]:
            result = False
            break
        
    if result:
        print('YES')
    else:
        print('NO')
    
    t -= 1