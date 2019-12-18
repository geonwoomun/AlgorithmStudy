# 5249 최소 신장 트리
# 프림 크루스칼 어려워서 일단 보류....
from collections import defaultdict, deque
T = int(input())

for t in range(1, T+1):
    endNode, edgeCount = map(int, input().split())

    dic = defaultdict(list)

    for _ in range(edgeCount):
        n1, n2, w = map(int, input().split())
        dic[n1].append((n2,w))
        dic[n2].append((n1,w))

    result = 999999
    for i in range(endNode+1):
        weight = [999999 for _ in range(endNode+1)]
        visit = set()
        q = deque()
        q.append(i)
        weight[i] = 0
        visit.add(i)
        while q:
            start = q.popleft()
            for n in dic[start]:
                node, w = n
                weight[node] = min(weight[node], w)
                if node not in visit:
                    visit.add(node)
                    q.append(node)
        result = min(result, sum(weight))

    print("#",end='')
    print(t, result)