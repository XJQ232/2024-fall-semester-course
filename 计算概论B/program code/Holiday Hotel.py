n = 1
d=[0]*100000;p=[0]*100000
while n!= 0:
    n= int(input())
    total = 0
    for i in range(n):
        d[i],p[i]= map(int,input().split())
    # check= [True]*n
    # d1=sorted(range(n),key=lambda x:d[x])
    # p1=sorted(range(n),key=lambda x:p[x])
    # total = n
    # for i in range(n):
    #     if check[i] == False:
    #         break
    #     for j in range(n):
    #         if d[j] < d[i] and p[j] < p[i]:
    #             check[i] =False
                # total -= 1
    d1=sorted(range(n),key=lambda x:d[x])
    p1=sorted(range(n),key=lambda x:p[x])
    curr = 0
    while True:
        n = min(p1.index(d1[curr]),d1.index[p1[curr]])
        if curr == n:
            break

    print(total)
