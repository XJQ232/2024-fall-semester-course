l1 = list(map(int,input().split(',')))
dp1 = l1.copy()
dp2 = [-float('inf')]+[0]*(len(l1)-1)
max1 = l1[0]
for i in range(1,len(l1)):
    dp1[i] = max(dp1[i],dp1[i-1]+l1[i])
    dp2[i] = max(dp2[i-1]+l1[i],dp1[i-1])
    max1 = max(max1,dp1[i],dp2[i])
# print(dp1,dp2)
print(max1)