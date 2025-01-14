n =int(input())
dp = [[0]*n for _ in range(n)]
num = [[] for _ in range(n)]
for _ in range(n):
    num[_] = list(map(int,input().split()))
dp [0][0] = num[0][0]
max1 = 0
for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            dp[i][j]=dp[i-1][j]+num[i][j]
        if j == i:
            dp[i][j]=dp[i-1][j-1]+num[i][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-1])+num[i][j]
        if i == n-1:max1 = max(max1,dp[i][j])
print(max1)