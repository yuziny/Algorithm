def solution(s):
    stack = []
    for i in s:  # 문자열 s크기만큼 반복
        if i == '(':
            stack.append('(')
        else: # ')'인 경우
            if stack == []: # 스택이 비어있는데 ')'가 들어올 때
                return False
            else: # 스택 안에 '('가 있고 ')'가 들어올 때
                stack.pop()
    if stack != []: # for문이 끝났는데 '('남아있을 때
        return False
    
    return True
