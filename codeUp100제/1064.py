a, b, c = map(int, input().split())

d = a > b and (b > c and c or b) or (a > c and c or a)

print(d)
