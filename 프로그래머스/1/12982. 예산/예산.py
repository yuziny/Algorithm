def solution(d, budget):
    answer = 0 # 가능한 부서 수
    for i in sorted(d):
        budget -= i
        if budget < 0:
            break
        answer += 1
        
    return answer