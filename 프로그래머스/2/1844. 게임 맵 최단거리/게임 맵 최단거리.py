from collections import deque
def solution(maps):
    answer = 0
    #상하좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    queue = deque()
    queue.append((0,0)) #0,0에서 시작
    
    while queue:
        x, y = queue.popleft()
        #상하좌우 이동 좌표
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            #미로의 행,열
            n = len(maps)
            m = len(maps[0])
            #이동가능한 범위 내, 벽이 아닌 경우
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                #다음 좌표 큐에 넣고
                maps[nx][ny] = maps[x][y]+1
                #최단거리 갱신
                queue.append((nx, ny))
    answer = maps[n-1][m-1]
    #도달할 수 없는 경우
    if answer == 1:
        answer = -1
    return answer