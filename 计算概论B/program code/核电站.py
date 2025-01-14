n,m = map(int,input().split())
dp0 = [1]*(n+1)
dp1 = [1]*(n+1)
for i in range(1,n+1):
    if i < m:
        dp0[i] = 1 << i-1
        dp1[i] = 1 << i-1
    else:
        dp0[i] = dp0[i-1] + dp1[i-1]
        dp1[i] = dp0[i-1] + dp1[i-1] - dp0[i-m]
    # print(dp0,dp1)
print(dp0[-1]+dp1[-1])