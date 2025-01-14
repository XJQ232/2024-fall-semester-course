n = int(input())
l1 = list(map(int,input().split()))
dp=[1]*n
max1=1
for i in range(1,n):
    for j in range(i):
        if l1[j] >= l1[i]:
            dp[i] = max(dp[i],dp[j]+1)
    if dp[i] > max1:
        max1 = dp[i]
print(max1)