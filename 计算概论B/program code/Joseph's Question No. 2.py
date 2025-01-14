while True:
    n,p,m=map(int,input().split())
    if n == 0:
        exit()
    check=[True]*n
    step= p-1
    str1=[]
    for i in range(n):
        curr = 0
        while curr < m:
            step = (step+1)%n
            if check[step]:
                curr +=1
        check[step]=False
        if step:
            str1.append(str(step))
        else:
            str1.append(str(n))
    print(','.join(str1))