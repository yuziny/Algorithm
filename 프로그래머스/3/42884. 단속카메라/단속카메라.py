def solution(routes):
    routes.sort(key = lambda x: x[1]) #진출지점 오름차순
    key = -30001
    cnt = 0 #카메라 수
    
    for route in routes:
        if route[0] > key: #진입지점이 key보다 크면 찍을 수 없음
            cnt += 1 #새 카메라 설치
            key = route[1] #진출지점에
            
    return cnt