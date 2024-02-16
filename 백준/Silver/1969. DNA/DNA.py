import sys
n, m = map(int, sys.stdin.readline().split())

list = []
s = ''
dna = ['A','C','G','T']
haming_distance = 0

for i in range(n):
    data = input()
    list.append(data)
    
for i in range(m):
    a_cnt, c_cnt, g_cnt, t_cnt = 0, 0, 0, 0
    for j in range(n):
        if list[j][i] == dna[0]:
            a_cnt += 1
        elif list[j][i] == dna[1]:
            c_cnt += 1
        elif list[j][i] == dna[2]:
            g_cnt += 1
        elif list[j][i] == dna[3]:
            t_cnt += 1
    cnt_list = [a_cnt, c_cnt, g_cnt, t_cnt]
    select_dna = dna[cnt_list.index(max(cnt_list))]
    s += select_dna
    for k in range(n):
        if list[k][i] != select_dna:
            haming_distance += 1
print(s)
print(haming_distance)