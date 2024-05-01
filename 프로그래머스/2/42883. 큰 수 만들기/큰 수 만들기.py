def solution(number, k):
    #맨 앞자리 크게 만들기 위한 임시저장
    stack = []
    
    #1231234
    for i in number:
        #스택이 비어있지않고, k가 남아있고, 스택의 맨 위 숫자가 i보다 작을 때까지
        while len(stack) > 0 and k > 0 and stack[-1] < i:
            stack.pop()
            k -= 1
        stack.append(i)
        
    #k > 0이면
    if k:
        return number[:-k]
    #k = 0이면
    else:
        return "".join(stack)