from collections import deque
def solution(n, computers):
    
    def bfs(i):
        q = deque()
        q.append(i)
        while q:
            i = q.popleft() #노드방문
            visited[i] = 1 #방문했음을 나타냄
            for a in range(n): #컴퓨터 개수만큼 방문
                if computers[i][a] and not visited[a]: #노드i와 a사이에 연결있고, 아직 방문안했는지 확인
                    q.append(a)
                    
    answer = 0         
    visited = [0 for i in range(len(computers))]
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
            
    return answer