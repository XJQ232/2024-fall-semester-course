m = int(input())
n = int(input())
l1 = list((input().split()))
for i in range(n):
    for j in range(i+1,n):
        if l1[j]+l1[i] > l1[i] + l1[j]:
            l1[i],l1[j] = l1[j],l1[i]
dp = ['0']*(m+1)
for i in range(n):
    for j in range(m,len(l1[i])-1,-1):
        
        dp[j] = str(max(int(dp[j]),int(dp[j-len(l1[i])]+l1[i])))
        # print(dp)
print(int(dp[-1]))