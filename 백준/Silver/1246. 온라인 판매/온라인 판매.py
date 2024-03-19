import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 달걀 수, 고객 수
p = [int(input()) for _ in range(m)] # 고객이 제시한 가격
p.sort() # 책정 가격 오름차순
res = 0 # 수익
target = 0 # 적정 가격

for i in range(m):
    egg = min(m - i, n) # 달갈보다 고객이 많으면 예외
    if res < p[i] * egg: # 현재 수익보다 달걀로 판매하는 수익이 더 크면
        res = p[i] * egg # 수익 초기화
        target = p[i] # 적정 가격 초기화
        
print(target, res)