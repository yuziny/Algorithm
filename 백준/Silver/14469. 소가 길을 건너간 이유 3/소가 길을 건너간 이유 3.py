import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a,b])
arr.sort() # 일찍 도착한 소부터
time = 0
for i in range(len(arr)):
    if time > arr[i][0]: # 다음 소가 이전 소 검문 받는 중에 도착하면
        time = time + arr[i][1] # 기다리는 시간: 이전 소 입장시간 + 다음 소 검문시간
    else: # 검문 다 받고 도착하면
        time = arr[i][0] + arr[i][1] # 기다리는 시간 없음: 다음 소 도착시간 + 그 소 검문시간
            
print(time)
