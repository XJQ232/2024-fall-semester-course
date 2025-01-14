l1 = [pow(2,i)-1 for i in range(13)]
dp = [0,1]
for i in range(2,13):
    ans = float("inf")
    for k in range(1,i):
        ans = min(ans,2*dp[k]+l1[i-k])
    dp.append(ans)
for i in range(1,13):
    print(dp[i])