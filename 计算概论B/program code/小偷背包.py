n,b=map(int,input().split())
value=list(map(int,input().split()))
weight=list(map(int,input().split()))
dp = [0]*(b+1)
max1 = 0
for i in range(n):
    for j in range(b,weight[i]-1,-1):
        dp[j]=max(dp[j],dp[j-weight[i]]+value[i])
        max1 = max(max1,dp[j])
print(max1)