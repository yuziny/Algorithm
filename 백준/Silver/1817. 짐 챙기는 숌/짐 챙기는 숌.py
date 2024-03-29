import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cnt = 0
if n == 0:
    print(0)
else:
    boxes = list(map(int, input().split()))
    weight = 0
    cnt = 1
    for box in boxes:
        if box + weight <= m:
            weight += box
        else:
            weight = box
            cnt += 1
    print(cnt)