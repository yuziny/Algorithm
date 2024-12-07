n = int(input())

ans = []
def hanoi(n, start, by, end):
    if n == 1:
        ans.append((start, end))
        return
    
    hanoi(n-1, start, end, by)
    ans.append((start, end))
    hanoi(n-1, by, start, end)
    
hanoi(n, 1, 2, 3)
print(len(ans))
for a in ans:
    print(*a)