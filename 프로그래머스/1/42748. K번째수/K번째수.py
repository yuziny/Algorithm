def solution(array, commands):
    answer = []
    
    for i,j,k in commands:
        res = array[i-1:j] #i부터 j까지 슬라이싱
        res.sort()
        answer.append(res[k-1])
    return answer