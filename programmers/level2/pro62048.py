# 프로그래머스 윈터코딩 멀쩡한 사각형

# def getGcd(w, h):
#     if (h == 0):
#         return w
#     return getGcd(h, w % h)

import math
def solution(w,h):
    if (w > h):
        w, h = h, w
    
    return w*h - (h + w - math.gcd(w,h))