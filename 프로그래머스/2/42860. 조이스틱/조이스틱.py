def solution(name):
    #조이스틱 조작 횟수
    answer = 0
    #좌우이동(커서)
    min_move = len(name)-1 #왼쪽에서 오른쪽 방향 이동(최대)
    
    #name을 순회하면서 알파벳char과 인덱스i 가져옴
    for i, char in enumerate(name):
        #A에서 해당문자까지의 거리, Z에서 해당 문자까지의 거리 중 최소값
        answer += min(ord(char)-ord('A'), ord('Z')-ord(char)+1)
        
        #현재 알파벳 다음부터 시작해 연속된 A문자열 찾기
        next = i + 1
        #name길이보다 작고 name[next]가 A인 동안
        while next < len(name) and name[next] == 'A':
            next += 1
        
        #기존, 연속된 A의 왼쪽시작, 연속된 A의 오른쪽 시작 방식 비교
        min_move = min([min_move, 2*i + len(name) - next, i + 2*(len(name) - next)])
        
    #알파벳 변경 횟수+좌우이동 횟수
    answer += min_move
    return answer