l1 = list(map(int,input().split()))
max1 = 0
len1 = len(l1)
l2 = []
for i in range(1,len1):
    l2.append(l1[i]-l1[i-1])
dp = [0]*len1
dp[0] = l2[0]
for i in range(1,len1):
    dp[i] = max(dp[i],dp[i-1]+l2[i-1])
    max1 = max(max1,dp[i])
print(max1)