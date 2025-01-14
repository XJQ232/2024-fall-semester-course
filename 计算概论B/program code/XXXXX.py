t = int(input())
for _ in range(t):
    n,m=map(int,input().split())
    l0=list(map(int,input().split()))
    l1=[x % m for x in l0]
    sum1 = sum(l1)%m
    if sum1:
        print(n)
    else:
        max1 = 0
        check = False
        for i in range(n):
            if l1[i] != sum1:
                check = True
                if i<=n//2:
                    if max1 <n-i-1:
                        max1 = n-i-1 
                else:
                    if max1 < i:
                        max1 = i
        if check:print(max1)
        if not check:
            print("-1")