import sys
input = sys.stdin.readline
n = int(input())

data = list(map(int, input().split()))
data.sort(reverse=True) #내림차순 정렬

result = []
for i in range(n):
    result.append(data[i] + 1 + i) #나무 자라는 시간 + 나무 심는데 하루 + 몇번째 나무
    
print(max(result) + 1) #며칠에 초대할 수 있는지

