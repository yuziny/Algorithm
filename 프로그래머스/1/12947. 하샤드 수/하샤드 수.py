def solution(x):
    answer = True
    
    if x % sum(map(int, list(str(x)))) == 0:
        answer = True
    else:
        answer = False
    return answer
