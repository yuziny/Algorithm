import sys
input = sys.stdin.readline

n = int(input())
s = input()

colors = {'B':0, 'R':0} # B칠할 횟수, R칠할 횟수 저장
colors[s[0]] += 1 #B횟수 증가시키기
for i in range(1, n):
    if s[i] != s[i-1]: #이전 값과 다르다면 횟수 증가
        colors[s[i]] += 1
result = min(colors['B'], colors['R']) + 1 #최솟값 구해서 +1

print(result)