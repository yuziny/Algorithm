def solution(n, times):
    answer = 0
    #가능한 최소값과 최대값 설정
    left = 1
    right = max(times) * n
    
    while left <= right:
        mid = (left + right) // 2
        people = 0
        
        for time in times:
            people += mid // time #해당 심사대에서 주어진 시간동안 심사받은 수 더하기
            if people >= n:
                break
                
        if people >= n:
            answer = mid
            right = mid-1
        else:
            left = mid+1
    return answer