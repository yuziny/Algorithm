import sys
input = sys.stdin.readline

arr = []
n = int(input())
for i in range(n):
    arr.append(int(input()))
    
arr.sort(reverse=True) # 할인되는 품목은 비싼거부터
sum = 0
for i in range(n):
    if i % 3 != 2:
        sum += arr[i]
print(sum)
