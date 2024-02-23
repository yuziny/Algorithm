import sys
n = int(sys.stdin.readline()) #후보수
dasom = int(sys.stdin.readline()) #다솜이 득표수
candi = []
cnt = 0
for i in range(n-1):
    masu = int(sys.stdin.readline()) #다른사람 득표수
    candi.append(masu)
if n == 1: #후보자가없다면 
    pass
else:
    while dasom <= max(candi): #다솜이가 최다득표 될 때까지
        dasom += 1 #다솜이에게 매수표
        cnt += 1
        candi[candi.index(max(candi))] -= 1 #최대값에서 하나 빼기
print(cnt)
        
    
