n = int( input())
str = input().split()
a=[0]*n
dp=[1]*n
max = 0
for i in range(n):
    a[i]=int(str[i])
    if i>0 and a[i]>=a[i-1]:
        dp[i]=dp[i-1]+1
    if dp[i] > max:
        max = dp[i]
print(max)

# a = list(map(int,input().split()))