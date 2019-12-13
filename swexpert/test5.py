# 전자키트
# 잘 모르겠어서 참고.
# dfs를 끝까지 갔다가 끝내면서 sub_result를 지워버리고 visited도 fasle로 다시 바꾸는게 중요하늗ㅅ.
# dfs로 해보려고 했는데 dfs 끝나고 지우면 된다는 생각을 못함.
# 너무 오래걸리지 않을까 걱정되서 안 해본 감도 있음.
def DFS(start):
    global sub_result, result, final_result

    if len(sub_result) == N-1:
        for i, j in sub_result:
            result += Battery[i][j]

        result += Battery[start][0]
        final_result.append(result)
        result = 0
        return

    for next in range(1, N):
        if not visited[next]:
            sub_result.append((start, next))
            visited[next] = True
            DFS(next)
            sub_result.remove((start, next))
            visited[next] = False


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    Battery = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    sub_result =  []
    result = 0
    final_result =[]
    DFS(0)

    print('#%d %d'%(tc, min(final_result)))