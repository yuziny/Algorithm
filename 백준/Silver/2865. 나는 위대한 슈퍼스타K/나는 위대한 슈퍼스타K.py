import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
skills = {}

for i in range(N):
    skills[i+1] = 0

for i in range(M):
    genre = list(map(float, input().split()))
    for j in range(0, N*2, 2):
        if genre[j+1] > skills[genre[j]]: # 기존사람의 능력보다 새로운 사람이 높다면
            skills[genre[j]] = genre[j+1]
score = sorted(list(skills.values()), reverse=True)
total_sum = sum(score[:K])
print('%.1f' % total_sum)