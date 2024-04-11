import sys
input = sys.stdin.readline
n = int(input())
ANA = list(map(int, input().split()))
benefit, result = 0, 0 # 최대 이익, 결과값

for i in range(n-1, -1, -1): # 뒤에서부터 가장 비싸게 팔 수 있는 날
    benefit = max(benefit, ANA[i]) # 최대 주가
    result = max(result, benefit-ANA[i]) # 최대값-i번째 주가
    
print(result)