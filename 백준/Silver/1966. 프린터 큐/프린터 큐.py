from collections import deque
import sys
t = int(sys.stdin.readline())

for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    queue = deque(list(map(int, sys.stdin.readline().split())))
    cnt = 0
    while queue:
        best = max(queue) # 현재 최대값 저장
        front = queue.popleft() 
        m -= 1 # 한 칸 앞으로
        
        if best == front: # 뽑은 게 제일 큰 숫자일 때
            cnt += 1 # 빠져나간 횟수
            if m < 0: # 뽑은 게 내 숫자 일 때
                print(cnt)
                break
        else: # 뽑은 게 제일 큰 숫자가 아니면
            queue.append(front) # 제일 뒤로
            if m < 0: # 제일 앞에서 뽑히면
                m = len(queue) -  1 # 제일 뒤로