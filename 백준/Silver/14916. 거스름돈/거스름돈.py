import sys
n = int(sys.stdin.readline())
cnt = 0
i = 0
while True:
    if n % 5 == 0: # 5의 배수 or 2로 거슬러주고 n = 0
        cnt += n // 5 # 5로 나눈 몫
        break
    else:
        n -= 2 # 5의 배수 아니면 2원씩 빼면서 5로 나누어 떨어질 때까지
        cnt += 1
    if n < 0: # 2백원씩 뺐더니 음수
        break
if n < 0:
    print(-1)
else:
    print(cnt)