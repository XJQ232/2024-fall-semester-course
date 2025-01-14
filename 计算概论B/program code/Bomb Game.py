A,B,K = map(int,input().split())
map1=[]
check=[]
max1 = 0
total = 0
for i in range(A):
    map1.append([])
    check.append([])
    for j in range(B):
        map1[i].append(0)
        check[i].append(True)
for _ in range(K):
    n,m,r,t=map(int,input().split())
    r=(r-1)//2
    n1 = max(0,n-r-1)
    n2 = min(A,n+r)
    m1 = max(0,m-r-1)
    m2 = min(B,m+r)
    if not t:
        for i in range(n1,n2):
            for j in range(m1,m2):
                check[i][j] = False
                map1[i][j] = 0
    else:
        for i in range(n1,n2):
            for j in range(m1,m2):
                if check[i][j]:
                    map1[i][j] += 1
                    if max1 < map1[i][j]:max1 = map1[i][j]
print(sum(map1[x].count(max1) for x in range(A)))