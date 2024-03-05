import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 줄 개수, 브랜드

pack = [0] * m # 세트 가격
one = [0] * m # 개당 가격
for i in range(m):
    pack[i], one[i] = map(int, input().split())
min_pack, min_one = min(pack), min(one)

if min_pack > min_one * 6: # 세트가 더 비싸다면
    print(n * min_one) # 낱개로 사면됨
else: # 세트가 싸다면
    # 먼저 한 세트 샀을 때
    if (n % 6) * min_one < min_pack: # (나머지 낱개 수 * 낱개 가격)이 더 싸다면
        print(((n // 6) * min_pack) + ((n % 6) * min_one))
    
    else:
        print(((n // 6) + 1) * min_pack)
    


    
