n = int(input())
l1 = list(map(int,input().split()))
dp = [0]*n
dp[0] = l1[0]
max1 = dp[0]
s = 0
e = float("inf")
ans =()
for i in range(1,n):
    if dp[i-1]+l1[i] < l1[i]:
        s = i
        dp[i] = l1[i]
    else:
        dp[i] = dp[i-1]+l1[i]
    if dp[i] > max1:
        max1 = dp[i]
        e= i
        ans=(s,e)
    # print(dp,s,e)
x,y= ans
print(max1,x+1,y+1)
    
