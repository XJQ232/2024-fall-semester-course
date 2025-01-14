r,n=map(int,input().split())
while r!=-1:
    l1=sorted(list(set(map(int,input().split()))))
    len1 = len(l1)
    curr = l1[0]
    total = 0
    check = False
    for i in range(0,len1-1):
        if l1[i] <= curr + r and l1[i+1] > curr + r:
            if check:
                total += 1
                curr = l1[i+1]
                check = False
            else:
                if l1[i+1] - l1[i] <= r:
                    curr = l1[i]
                    check = True
                else:
                    total += 1
                    curr = l1[i+1]

    if curr == l1[-1]:
        total += 1
    print(total)
    r,n=map(int,input().split())
