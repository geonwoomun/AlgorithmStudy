def solution(board, moves):
    changeList = changeXY(board)
    resultList = []
    answer = 0
    for value in moves:
        if len(changeList[value-1]) != 0:
            if len(resultList) == 0:
                resultList.append(changeList[value-1].pop(0))
            else:
                doll = changeList[value-1].pop(0)
                if doll ==  resultList[len(resultList)-1]:
                    resultList.pop()
                    answer += 2       
                else:
                    resultList.append(doll)    

    return answer

def changeXY(board):
    changeList = [[] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j] != 0):
                changeList[j].append(board[i][j])
    return changeList

board =[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]	

print(solution(board, moves))