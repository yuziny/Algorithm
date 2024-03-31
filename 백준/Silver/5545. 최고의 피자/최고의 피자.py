import sys
input = sys.stdin.readline
n = int(input())
a, b = map(int, input().split())
dow = int(input())
data = []
for i in range(n):
    data.append(int(input()))
data.sort(reverse=True) #칼로리 내림차순
money = a
kalori = dow
won = dow / a

for i in data:
    money += b
    kalori += i
    now = kalori / money
    if won < now:
        won = now
    else:
        break
print(int(won))