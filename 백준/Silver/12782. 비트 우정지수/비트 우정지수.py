import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(str, input().split())
    one = 0
    zero = 0
    for i in range(len(M)):
        if N[i] != M[i]:
            if M[i] == '1':
                one += 1
            else:
                zero += 1
    print(max(one, zero))