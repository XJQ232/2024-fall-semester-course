n,k = map(int,input().split())
stack=[];max1=0
for _ in range(n):
    x,y = map(int,input().split())
    stack.append((x,y))
    max1 = max(max1,y)
dp=[1]*(max1+1)
sum1 = [0]*(1+max1)
for i in range(1,max1+1):
    if i < k:
        dp[i]=1
    else:
        dp[i] = (dp[i-1]+dp[i-k])%1000000007
    sum1[i] = (sum1[i-1]+dp[i])%1000000007
for _ in range(n):
    print((sum1[stack[_][1]]-sum1[stack[_][0]-1])%1000000007)