
from collections import deque

n, m = map(int, input().split())
pick = list(map(int, input().split()))
q = deque([i for i in range(1, n+1)])
cnt = 0

for i in pick:
    while True:
        if q[0] == i:
            q.popleft() #찾고자하는 원소면 꺼내기
            break
        else:
            if q.index(i) < len(q)/2: #가까운쪽
                while q[0] != i:
                    q.append(q.popleft())
                    cnt += 1
            else:
                while q[0] != i:
                    q.appendleft(q.pop())
                    cnt += 1
print(cnt)