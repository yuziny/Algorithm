import sys
n = int(sys.stdin.readline()) # 지방 정부 수
budget = list(map(int, sys.stdin.readline().split())) # 예산 요청
m = int(sys.stdin.readline()) # 총 예산
budget.sort() # 오름차순 정렬

start, end = 1, budget[-1] # 예산 최소, 최대값
while start <= end:
    mid = (start+end)//2 # 상한액
    cost = 0 # 요청 금액
    for i in budget:
        if i > mid: # 요구 예산이 상한액보다 크면
            cost += mid # 상한액 할당
        else: # 작으면
            cost += i # 요구 예산 할당
            
    if cost > m: # 총 예산보다 크면
        end = mid - 1 # 최댓값 줄임
    else: # 작으면
        start = mid + 1 # 최소값 늘림
print(end)