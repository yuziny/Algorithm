from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    card = input().split()
    q = deque()
    q.append(card[0])
    st = card[0] # 기준
    
    for i in range(1, len(card)):
        if st >= card[i]: # 기준보다 작으면
            q.appendleft(card[i]) # 왼쪽
            st = card[i] # 기준 이동
        else:
            q.append(card[i])
            
    print(''.join(q))