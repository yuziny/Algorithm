import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    
    cnt_b = 0
    cnt_w = 0
    data1 = input()
    data2 = input()
    
    for i in range(N):
        if data1[i] != data2[i]:
            if data1[i] == 'B':
                cnt_b += 1
            else:
                cnt_w += 1
    print(max(cnt_b, cnt_w))