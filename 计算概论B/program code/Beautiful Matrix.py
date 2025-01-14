a=['']*5
for i in range(5):
    a[i]=input().split()
    for j in a[i]:
        if j == '1':
            print(abs(i-2)+abs(a[i].index(j)-2))