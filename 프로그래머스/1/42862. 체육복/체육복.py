def solution(n, lost, reserve):
    #정렬 [2,3,4] [1,3,5]
    lost.sort()
    reserve.sort()
    
    #lost와 reserve 같은 값 제거 [3]
    for i in reserve[:]:
        if i in lost:
            lost.remove(i)
            reserve.remove(i)
            
    #reserve에서 lost번호 확인하고 빌려주기
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
            
    
    return n - len(lost)