import sys
n, c = map(int, sys.stdin.readline().split()) # 집, 공유기 수
house = [int(sys.stdin.readline()) for _ in range(n)] # 각 집의 위치
house.sort()

start = 1
end = house[-1] - house[0] # 가장 멀리 떨어진 두 집 사이 거리
answer = 0
while start <= end:
    mid = (start+end)//2 # 공유기 설치할 수 있는 최적의 거리
    current = house[0] # 첫번째 집 위치 저장
    cnt = 1 # 설치된 공유기
    for i in range(1, len(house)):
        if house[i] >= current + mid: # 현재 집 위치가 current에서 mid이상 떨어졌는지
            current = house[i] # 설치한 집 위치 업뎃
            cnt += 1 
        
    if cnt < c: # 설치된 공유기 수가 목표보다 적을 때
        end = mid - 1 # 공유기 사이 거리 줄이기
    else:
        start = mid + 1 # 공유기 사이 거리 늘리기
        answer = mid
print(answer)