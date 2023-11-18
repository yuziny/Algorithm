import sys
sys.setrecursionlimit(10000) # 재귀호출 최대횟수 늘리기
T = int(sys.stdin.readline())

def dfs(x,y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    
    if graph[x][y] == 1: # 배추가 있으면 방문했으니까 0으로 변경
        graph[x][y] = 0
        dfs(x-1, y) # 배추가 있는 곳의 상,하,좌,우 확인
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True # 배추흰지렁이 cnt증가
    return False

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0]*(M) for _ in range(N)] # 0으로 초기화
    cnt = 0 # 배추흰지렁이의 수
    
    for _ in range(K): # 배추가 심어져있는 위치의 개수K만큼 배추 심기
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1 # 위치를 입력받아 그 위치의 0을 1로 변경

    for i in range(N): # 인접한 배추들 당 배추흰지렁이 증가
        for j in range(M):
            if dfs(i,j) == True:
                cnt += 1
    print(cnt)
    