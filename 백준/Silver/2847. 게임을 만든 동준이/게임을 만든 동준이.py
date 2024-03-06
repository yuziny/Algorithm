import sys
input = sys.stdin.readline
n = int(input())
score = []
for i in range(n):
    score.append(int(input()))
    
cnt = 0
for i in reversed(range(n-1)):
    if score[i+1] <= score[i]:
        minus = score[i] - score[i+1] + 1
        score[i] = score[i] - minus
        cnt += minus
print(cnt)