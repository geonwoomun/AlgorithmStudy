w, h, b = map(int, input().split())

result = (w* h * b) / 8

print("{0:.2f} MB".format(result/(1024*1024)))