n = int(input())
dp=[0]*n
stack=[]
for _ in range(n):
    x,y,z= input().split()
    if x[0]=='1':
        s=(int(x[2:])-6)
    else:
        s=(int(x[2:])+25)
    if y[0]=='1':
        e=(int(y[2:])-6)
    else:
        e=(int(y[2:])+25)
    stack.append((s,e,int(z)))
dp=[0]*46
for i in range(1,46):
    dp[i]=dp[i-1]
    for s,e,z in stack:
        if e == i:
            dp[i] = max(dp[i],dp[s-1]+z)
print(dp[-1])