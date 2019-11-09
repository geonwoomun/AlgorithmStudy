# 카카오 겨울인턴쉽 코딩테스트
# 인형 뽑기 ? 그런거였는데 답이 맞긴 맞았다.
# 1,2,3번은 효율성 테스트가 없어서 좋았다.
def solution(board, moves):
    answer = 0
    box = []
    for move in moves:
        for doll in board :
            if(doll[move-1] != 0):
                box.append(doll[move-1])
                doll[move-1] = 0
                break
        if(len(box) >= 2):
            if(box[len(box) -1] == box[len(box) -2]):
                box.pop()
                box.pop()
                answer +=2
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]	
solution(board, moves)