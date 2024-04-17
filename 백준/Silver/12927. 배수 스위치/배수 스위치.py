N = list(input())
N.insert(0,'N')

result = 0
for i in range(1, len(N)):
    if N[i] == 'Y':
        for j in range(i, len(N), i):
            if N[j] == 'Y': # Y일 경우 i의 배수 번호가지는 전구 반전
                N[j] = 'N'
            else:
                N[j] = 'Y'
                
        result += 1
print(result)