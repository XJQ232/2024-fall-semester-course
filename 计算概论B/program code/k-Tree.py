n,k,d = map(int,input().split())
dp1=[1]+[0]*(n)
dp2=[0]*(n+1)
for i in range(1,n+1):
    for j in range(1,k+1):
        if i >= j:
            if j >= d:
                dp2[i] = dp2[i]+dp1[i-j]+dp2[i-j]
            else:
                dp1[i] = dp1[i] + dp1[i-j]
                dp2[i] = dp2[i] + dp2[i-j]
            dp1[i] %= 1000000007
            dp2[i] %= 1000000007
        else:
            break
print(dp2[n])