T,n = map(int,input().split())
dp = [0] +[-1]*(T)

time = []
weight = []
for _ in range(n):
    x,y = map(int,input().split())
    if x<= T:
        for i in range(T-x,-1,-1):
            if dp[i] >= 0:
                dp[i+x]=max(dp[i+x],dp[i]+y)
        # print(dp)
print(dp[-1])   