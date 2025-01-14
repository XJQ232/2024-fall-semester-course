n = int(input())
l1 = list(map(int,input().split()))
dp = [1]*n
max1 = 0
for i in range(n):
    for j in range(i):
        if l1[j] < l1[i]:dp[i]=max(dp[i],dp[j]+1)
    max1 = max(dp[i],max1)
# print(dp)
print(max1)