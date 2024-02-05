def d(n):
    num = list(str(n))
    answer = 0
    for i in range(len(num)):
        answer += int(num[i])
    answer = answer + n
    return answer

answers = set()
for i in range(10000):
    answers.add(d(i))
for m in range(1,10001):
    if m not in answers:
        print(m)