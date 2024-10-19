import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
ans = 0

def dfs(n):
    for i in task[n]:
        if check[i]: continue
        check[i] = 1
        if not visited[i] or dfs(visited[i]):
            visited[i] = n
            return 1
    return 0
    
n, m = map(int, input().split())
task = [[]] + [list(map(int, input().split()))[1:] for _ in range(n)]
visited = [0]*(m+1)

for i in range(1, n+1):
    check = [0] * (m+1)
    if dfs(i):
        ans += 1
print(ans)

