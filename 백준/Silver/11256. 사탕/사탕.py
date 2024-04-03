import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    j, n = map(int, input().split())
    data = []
    for _ in range(n):
        a, b = map(int, input().split()) # 가로 세로
        data.append(a*b)
        
    data.sort(reverse=True) # 상자개수 최소
    result = 0
    for i in range(len(data)):
        j -= data[i] # 사탕개수 - 상자크기
        result += 1
        if j <= 0: # 사탕개수 0 이하면 상자에 넣을 사탕 없음
            break
    print(result)