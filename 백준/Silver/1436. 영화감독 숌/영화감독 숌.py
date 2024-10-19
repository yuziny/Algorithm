n = int(input())
    
cnt = 0
num = 666
while True:
    str_num = str(num)
    if '666' in str_num:
        cnt += 1
        
    if n == cnt:
        break
    num += 1
print(num)