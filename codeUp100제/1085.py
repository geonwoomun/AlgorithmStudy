h, b, c, s = map(int, input().split())

result = (h*b*c*s) / 8

print("{0:.1f} MB".format(result/(1024*1024)))