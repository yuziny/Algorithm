import sys
n = int(sys.stdin.readline()) # 전체 사람 수
start, end = map(int, sys.stdin.readline().split()) # 촌수를 구해야하는 두 명
m = int(sys.stdin.readline()) # 부모자식들 간의 관계 개수

graph = [[] for i in range(n+1)] # start와 1촌인 사람들이 graph[start]에 들어감
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n+1) # 간선이 없을 경우 -1출력하기위해 초기화

result = []
def dfs(v, cnt):
    cnt += 1
    visited[v] = True
    # 찾는 사람에 도착했을 때
    if v == end:
        result.append(cnt)
    for i in graph[v]:
        if not visited[i]:
            dfs(i, cnt)
            
dfs(start, 0)
if len(result) == 0:
    print(-1)
else:
    print(result[0] - 1)
