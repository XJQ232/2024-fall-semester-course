from bisect import bisect_left
n = int(input())
l1 = list(map(int,input().split()))
l1_ = [-j for  j in l1]
dp = [0] * (n+1)
for i in l1_:
    id1 = bisect_left(dp,i)
    dp[id1] = i
print(bisect_left(dp,0))