from collections import deque
n = int(input()) #컴퓨터
v = int(input()) #연결선
graph = [[] for i in range(n+1)]
visited = [0]*(n+1) #방문여부

for i in range(v):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a] #양방향
    
visited[1] = 1
Q = deque([1])
while Q:
    c = Q.popleft()
    for j in graph[c]:
        if visited[j] == 0:
            Q.append(j)
            visited[j] = 1
print(sum(visited)-1)