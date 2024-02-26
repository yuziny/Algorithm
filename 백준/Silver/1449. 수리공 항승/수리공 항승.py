n, l = map(int, input().split()) #수리할 곳 개수, 테이프 길이
data = list(map(int, input().split()))
data.sort() #오름차순 정렬

cnt = 1
start = data[0]
end = start + l

for i in data:
    if i >= start+l:
        cnt += 1
        start = i

print(cnt)