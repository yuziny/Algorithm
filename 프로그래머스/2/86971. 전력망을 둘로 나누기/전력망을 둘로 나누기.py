from collections import deque
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True #현재노드 방문
    cnt = 0
    while queue:
        v = queue.popleft()
        cnt += 1
        for i in graph[v]: #해당 원소와 연결된 방문 안한 원소 큐에 삽입
            if not visited[i]:
                queue.append(i)
                visited[i] = True #방문처리
    return cnt

def solution(n, wires):
    answer = n-2 #두 전력망이 갖게 되는 송전탑 개수 차이의 절대값 중 최대값
    for i in range(len(wires)):
        tmp = wires.copy()
        graph = [[] for i in range(n+1)]
        visited = [False] * (n+1)
        tmp.pop(i)
        for wire in tmp:
            x, y = wire
            graph[x].append(y)
            graph[y].append(x)
        for idx, g in enumerate(graph):
            if g != []: #다른 송전탑과 연결된 송전탑을 시작점으로
                start = idx
                break
        cnts = bfs(graph, start, visited) #연결된 송전탑 개수
        other_cnts = n - cnts
        if abs(cnts - other_cnts) < answer:
            answer = abs(cnts - other_cnts)
    return answer