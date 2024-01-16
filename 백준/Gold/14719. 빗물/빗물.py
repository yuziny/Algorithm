h, w = map(int, input().split())
block = list(map(int, input().split()))
answer = 0

for i in range(1, w-1): # 맨 왼쪽과 맨 오른쪽 제외
    left = max(block[:i]) # 왼쪽에서 제일 높은 블록
    right = max(block[i+1:]) # 오른쪽에서 제일 높은 블록
    m = min(left, right) # 그 중에서 가장 낮은 블록
    if m > block[i]: # 현재 블록이 m보다 낮아야 빗물이 고임
        answer += m - block[i]
print(answer)