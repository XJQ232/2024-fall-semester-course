from itertools import combinations

n = int(input())
l1=[]
l = list(combinations(range(n),2))
while len(l1) < n**2:
    l1.extend(list(map(int, input().split())))
matrix = []
for i in range(n):
    matrix.append(l1[i*n:(i+1)*n])
max1 = 0
# print(l,matrix )
for s,e in l:
    sum1=[0]*n
    for i in range(s,e+1):
        for j in range(n):
            sum1[j]+=matrix[i][j]
    dp=[0]*n
    dp[0]=sum1[0]
    for i in range(1,n):
        if dp[i-1]>=0:
            dp[i]=dp[i-1]+sum1[i]
        else:
            dp[i]=sum1[i]
        max1=max(max1,dp[i])
print(max1)