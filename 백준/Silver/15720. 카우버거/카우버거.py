import sys
input = sys.stdin.readline

b, c, d = map(int, input().split())
burger = list(map(int, input().split()))
side = list(map(int, input().split()))
beverage = list(map(int, input().split()))
# 가격 비싼 순 정렬
burger.sort(reverse=True)
side.sort(reverse=True)
beverage.sort(reverse=True)

total = sum(burger) + sum(side) + sum(beverage)
print(total)

for i in range(min(len(burger), len(side), len(beverage))):
    temp = (burger[i] + side[i] + beverage[i])
    total -= temp//10
print(total)