import sys
input = sys.stdin.readline

n = int(input())
m = sorted([int(input()) for _ in range(n)], reverse=True)
answer = -1

for i in range(n-2):
    if m[i] < m[i+1] + m[i+2]: # 두변의 길이의 합보다 작아야됨
        answer = m[i] + m[i+1] + m[i+2]
        break
print(answer)
    