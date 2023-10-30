import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
# (0,3)(1,2)(2,1)(3,-3)(4,-1)
q = deque(enumerate(map(int, input().split()))) 
res = []
while q:
    idx, num = q.popleft() # 제일 앞의 요소 삭제(종이:3)
    res.append(idx+1) # 1번 풍선 터뜨린거 저장
    if num > 0: 
        q.rotate(-(num-1)) # 1번 풍선 터뜨렸기 때문에, num-1 반시계방향 회전
    else:
        q.rotate(-num)
        
print(' '.join(map(str, res)))
    
