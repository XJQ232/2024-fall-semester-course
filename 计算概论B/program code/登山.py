from bisect import bisect_left
n = int(input())
l1 = list(map(int,input().split()))
dp1=[1]*n
dp2=[1]*n
for i in range(1,n):
    for j in range(i):
        if l1[j]<l1[i]:
            dp1[i]= max(dp1[i],dp1[j]+1)
l1.reverse()
for i in range(1,n):
    for j in range(i):
        if l1[j]<l1[i]:
            dp2[i]= max(dp2[i],dp2[j]+1)
dp2.reverse()
max1= 0
# print(dp1,dp2)
for i in range(n):
    max1 = max(max1,dp1[i]+dp2[i]-1)
print(max1)