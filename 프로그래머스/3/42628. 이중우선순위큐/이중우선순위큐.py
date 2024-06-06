import heapq as hq
def solution(operations):
    q = []
    for i in operations:
        x, num = i.strip().split()
        if x == 'I':
            hq.heappush(q, int(num))
        elif x == 'D' and q:
            if num == '-1':
                hq.heappop(q)
            elif num == '1':
                q.pop()
                
    return [max(q), min(q)] if q else [0,0]