from bisect import bisect_left
n = int(input())
l1 = list(map(int,input().split()))
max1= l1[0]
dp=l1.copy()
for i in range(1,n):
    for j in range(i):
        if l1[j]<l1[i]:
            dp[i]=max(dp[i],dp[j]+l1[i])
    max1=max(max1,dp[i])
print(max1)
