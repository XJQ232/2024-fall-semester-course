n ,amount =map(int,input().split())
dp = [float("inf")]*(amount+1)
check = [False]*(amount+1)
l1 = list(map(int,input().split()))
for i in l1 :
    if i <= amount:
        dp[i] = 1
for i in range(1,amount+1):
    temp = dp[i]
    for j in l1:
        if i > j:
            temp = min(temp,dp[i-j]+1)
    if temp != dp[i]:
        dp[i] = temp
        check[i] =True
print(dp[amount] if check[amount] else "-1")