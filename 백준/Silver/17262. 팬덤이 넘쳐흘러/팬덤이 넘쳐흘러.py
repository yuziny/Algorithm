n = int(input())
fans = []
for _ in range(n):
    fans.append(list(map(int, input().split())))
    
a = sorted(fans, key=lambda x: x[0])
b = sorted(fans, key=lambda x: x[1])

result = a[-1][0] - b[0][1]
if result <= 0:
    print(0)
else:
    print(result)