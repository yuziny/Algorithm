k = int(input())
for i in range(k):
    data=list(map(int,input().split()))
    data1=data[1:]
    data1.sort(reverse=True)
    max_gap=0
    for j in range(len(data1)-1):
        if abs(data1[j+1]-data1[j])>max_gap:
            max_gap=abs(data1[j+1]-data1[j])
    print("Class",i+1)
    print("Max %d, Min %d, Largest gap %d" %(data1[0],data1[-1],max_gap))