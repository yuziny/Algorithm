import sys
s = sys.stdin.readline().strip()
n = 0
while len(s):
    n += 1
    num = str(n)
    while len(num) and len(s):
        if num[0] == s[0]: #n 앞자리가 s 앞자리랑 같으면
            s = s[1:]
        num = num[1:]
print(n)