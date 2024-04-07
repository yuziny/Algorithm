import sys

n, k = map(int, sys.stdin.readline().split())
li = sorted(list(map(int, sys.stdin.readline().split())))
sum = 0
for i in range(1, k+1):
    sum += li[-i] - i + 1
print(sum)
