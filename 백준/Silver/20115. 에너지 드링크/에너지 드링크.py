import sys
input = sys.stdin.readline
n = int(input())
drinks = list(map(int, input().split()))
drinks.sort() # 오름차순정렬

total = drinks[-1] # 최댓값
for i in range(n-1):
    total += drinks[i]/2 

print(total)