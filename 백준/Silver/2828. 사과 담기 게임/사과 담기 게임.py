import sys
input = sys.stdin.readline
n, m = map(int, input().split()) #스크린 n칸, 바구니 m칸
j = int(input()) #떨어지는 사과 개수
left = 1 #가장 처음 바구니 왼쪽 m칸 차지
right = m
cnt = 0 #바구니 이동거리 합산

for _ in range(j):
    position = int(input()) #사과 개수j만큼 반복문 돌려 떨어지는 위치 입력받기
    
    #사과가 바구니 안에 떨어지면
    if left <= position and right >= position:
        continue
    #왼쪽에 가깝게 떨어지면
    elif left > position:
        cnt += (left-position) #왼쪽 좌표값에서 떨어지는 위치 빼주기
        right -= (left-position) #왼쪽으로 움직인만큼 오른쪽에서 빼주기
        left = position #현재 사과가 떨어진 위치
    #오른쪽에 가깝게 떨어지면
    else:
        cnt += (position-right)
        left += (position-right)
        right = position
        
print(cnt)