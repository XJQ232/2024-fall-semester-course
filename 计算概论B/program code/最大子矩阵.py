from itertools import permutations
n = int(input())
l1= []
while len(l1) < n**2:
    l1.extend(map(int,input().split()))
matrix1 = [[0]*n for _ in range(n)]
for i in range(n**2):
    matrix1[i//n][i%n] = l1[i]
max1 = 0
print(matrix1)
for i in range(n):
    sum1= [0]*n
    for column in range(i):
        for line in range(n):
            sum1[line] += matrix1[line][column]
    print(sum1)
    dp = [sum1[i] for i in range(n)]
    max1 = max(max1,dp[0])
    for k in range(1,n):
        print(dp)
        if dp[k-1] >= 0:
            dp[k] += dp[k-1]
        max1 = max(dp[k],max1)
print(max1)