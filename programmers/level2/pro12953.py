# 프로그래머스 N개의 최소공배수
# gcd는 최대공약수를 구하는 것임
# 두개를 곱한 것을 / 최대공약수로 나누면 최소공배수가 됨.
# 그래서 계속 그거가지고 구해나간다~.
def gcd(a, b):
    if a < b :
        a,b = b,a
    while b != 0 :
        a, b = b, a % b
    return a
def solution(arr):
    temp = arr[0] * arr[1] / gcd(arr[0],arr[1])
    for i in range(2,len(arr)):
        temp = temp*arr[i] / gcd(temp,arr[i])
    return int(temp)

print(solution([2,6,8,14]))