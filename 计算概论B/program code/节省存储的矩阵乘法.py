n,m1,m2=map(int,input().split())
matrix1=[[0]*n for _ in range(n)]
matrix2=[[0]*n for _ in range(n)]
for i in range(m1):
    x,y,z= map(int,input().split())
    matrix1[x][y]=z
for i in range(m2):
    x,y,z= map(int,input().split())
    matrix2[x][y]=z
for i in range(n):
    for j in range(n):
        temp = 0
        for k in range(n):
            temp+=matrix1[i][k]*matrix2[k][j]
        if temp:
            print(i,j,temp)