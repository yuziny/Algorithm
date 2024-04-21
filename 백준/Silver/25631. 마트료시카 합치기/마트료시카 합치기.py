import sys
input = sys.stdin.readline
n = int(input())
ma = list(map(int, input().split()))

cnt = 0
while len(ma) > 0:
    temp = set(sorted(ma))
    for i in temp:
        del ma[ma.index(i)]
    cnt += 1
print(cnt)