import sys

input = sys.stdin.readline
t = int(input())

# 이동방향 초기화
dx = [0, -1, 0, 1] 
dy = [1, 0, -1, 0] 
for _ in range(t):
    order = list(map(str, input().strip()))
    dir = 0 # 현재 방향 초기화 북0, 서1, 남2, 동3
    min_x, min_y, max_x, max_y = 0, 0, 0, 0
    x, y = 0, 0 # 현재 좌표 초기화
    for ord in order:
        if ord == 'F': # 전진
            x += dx[dir]
            y += dy[dir]
            
        elif ord == 'B': # 후진
            x -= dx[dir]
            y -= dy[dir]
            
        elif ord == 'L': # 왼쪽
            if dir == 3: # 동쪽이면 북쪽
                dir = 0
            else:
                dir += 1 # 시계 반대 방향 회전
        elif ord == 'R': # 오른쪽
            if dir == 0: # 북쪽이면 동쪽
                dir = 3
            else:
                dir -= 1 # 시계 방향 회전
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        
    print(abs(max_x - min_x) * abs(max_y - min_y))