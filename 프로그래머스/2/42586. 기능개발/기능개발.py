import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    q = deque()
    
    # 작업을 수행하는데 며칠 걸리는지 계산
    for i in range(len(progresses)):
        # (100% - 30%) / 30% = 2.5를 올림하여 3일 동안 작업 후 배포 가능
        progress_duration = math.ceil((100 - progresses[i])/speeds[i])
        # q에 각 작업이 며칠 걸리는지 추가
        q.append(progress_duration)
        
    while q: # q가 비어있지 않는 동안
        end_day = q.popleft() # 작업 종료의 기준이 되는 날짜
        cnt = 1
        
        while q: # q에서 작업을 하나씩 가져와 맨 앞과 함께 배포될 수 있는지
            comp_end_day = q.popleft() # 작업 종료일 비교
            if comp_end_day <= end_day: # 같이 배포될 수 있으면 cnt 증가
                cnt += 1
            else: # 종료일보다 이후에 끝나는 경우
                q.appendleft(comp_end_day) # 다시 q의 맨 앞에 추가
                break
        answer.append(cnt)
    return answer