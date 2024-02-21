import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    rank = [list(map(int, input().split())) for _ in range(N)]
    rank_sort = sorted(rank) # 오름차순
    top = 0 # 첫번째 사람 면접 순위
    result = 1 # 첫번째 사람 채용
    
    for i in range(1, len(rank_sort)):
        if rank_sort[i][1] < rank_sort[top][1]:
            top = i
            result += 1
    print(result)