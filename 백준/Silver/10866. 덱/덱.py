import sys
n = int(sys.stdin.readline())
com = [list(sys.stdin.readline().split()) for _ in range(n)]

deque = []
for i in com:
    lenD = len(deque)
    if i[0] == 'push_front':
        deque.insert(0, i[1]) # 0번 인덱스에 삽입
    elif i[0] == 'push_back':
        deque.append(i[1])   # deque 가장 뒤에 입력받은 수
    elif i[0] == 'pop_front':
        if lenD == 0: # deque의 길이
            print(-1)
        else:
            print(deque[0])
            deque.pop(0)
    elif i[0] == 'pop_back': # 리스트의 -1번째는 리스트의 마지막
        if lenD == 0:
            print(-1)
        else:
            print(deque[-1])
            deque.pop(-1)
    elif i[0] == 'size':
        print(lenD) # 배열의 길이가 deque의 정수 개수
    elif i[0] == 'empty':
        if lenD == 0:
            print(1)
        else:
            print(0)
    elif i[0] == 'front':
        if lenD == 0:
            print(-1)
        else:
            print(deque[0])
    elif i[0] == 'back':
        if lenD == 0:
            print(-1)
        else:
            print(deque[-1])
        