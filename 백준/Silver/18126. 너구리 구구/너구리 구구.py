import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(node, cnt):
    global total
    visit[node] = True # 각 노드의 방문 여부 나타내는 리스트
    for i, j in graph[node]:
        if not visit[i]: # 방문하지 않았다면
            total = max(total, cnt+j) # 최대경로의 가중치 합 저장
            dfs(i, cnt+j)
            
N = int(input()) # 노드의 수
graph = [[] for _ in range(N+1)] # 노드와 가중치 저장

for i in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # a와 연결된 노드 및 가중치 리스트
    graph[b].append((a, c))
    
total = 0
visit = [False]*(N+1)
dfs(1, 0)
print(total)