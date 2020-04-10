#프로그래머스 윈터코딩 방문길이
def solution(dirs):
    move = {
        "U" : (0,1),
        "L" : (-1, 0),
        "R" : (1, 0),
        "D" : (0,-1)
    }
    nowX, nowY = [5,5]
    answer = 0
    check = set()
    for value in list(dirs):
        moveX, moveY = move[value]
        if 0 <= nowX + moveX <= 10 and 0 <= nowY + moveY <= 10: # 좌표평면을 벗어나지 않으면.
            nX, nY = nowX + moveX, nowY + moveY
            if (nowX, nowY, nX, nY) not in check:
                check.add((nowX, nowY, nX, nY))
                check.add((nX, nY, nowX, nowY))
                answer += 1
            nowX = nX
            nowY = nY 

    return answer


dirs = ""

s = ((1,2), (2,1))
p = ((2,1), (1,2))

print(s == p)