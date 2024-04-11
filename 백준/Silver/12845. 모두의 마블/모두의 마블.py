import sys
input = sys.stdin.readline
n = int(input())
cards = list(map(int, input().split()))
cards.sort(reverse=True)
level = cards[0]
gold = 0

for card in cards[1:]:
    gold += level + card # 앞에서부터 더하면서 골드 누적
    if level >= card:
        pass
    else:
        level = card # 높은 값으로 갱신
print(gold)