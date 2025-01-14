n = int(input())
matrix = [[] for _ in range(n)]
for i in range(n):
    matrix[i]= list(map(int,input().split()))
m = (n-1)//2 + 1
sum1 = [0] * m
for t in range(m):
    for i in range(t,n-t):
        for j in range(t,n-t):
            sum1[t] += matrix[i][j]
max1 = 0
for i in range(m-1):
    sum1[i] -= sum1[i+1]
print(max(sum1))
