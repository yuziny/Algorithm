import sys
input = sys.stdin.readline
n, k = map(int, input().split())

check = k*(k+1) // 2 # k개의 바구니가 있을 때 필요한 공의 개수 1~k합

if n < check: # 모든 바구니에 다른 개수의 공 못 넣음
    print(-1)
elif (n - check) % k == 0: # k의 배수라면 모든 바구니에 동일 개수 넣음
    print(k-1) # 가장 많은 공의 개수와 적은 개수 차이 같음
else: # k의 배수 아니라면 1~k-1 사이의 값
    print(k) # 가장 많은 바구니부터 적은 순으로 공 추가하면 차이는 k