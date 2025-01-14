n = int(input())
for _ in range(n):
    m = int(input())
    check = [False]*m
    a=[]
    b=[]
    grid=[0]*100
    total = 0
    for __ in range(m):
        l1=list(map(int,input().split()))
        a.append(l1[0])
        b.append(l1[1])
        for i in range(a[__],b[__]+1):
            grid[i] += 1
    for i in range(m):
        if not check[i]:
            total +=1
            check[i] = True
            max1 = 0
            for j in range(a[i],b[i]+1):
                if max1 < grid[j]:
                    max1 = grid[j]
            for j in range(a[i],b[i]+1):
                if max1 == grid[j]:
                    for k in range(m):
                        if a[k] <= j and j<=b[k]:
                            check[k]=True
    print(total)