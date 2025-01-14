n,m=map(int,input().split())
matrix = []
max1 = 0
l1=[]
for _ in range(n):
    l1=list(map(int,input().split()))
    matrix.append(l1)
for i in range(n):
    for j in range(m):
        curr = matrix[i][j]*(matrix[0][j]*1000+matrix[i][-1]*100+matrix[-1][j]*10+matrix[i][0])
        if max1 < curr:
            max1 = curr
print(max1)