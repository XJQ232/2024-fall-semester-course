m1,n1=map(int,input().split())
mat1=[[0]*n1 for _ in range(m1)]
for i in range(m1):
    mat1[i]=list(map(int,input().split()))
m2,n2=map(int,input().split())
mat2=[[0]*n2 for _ in range(m2)]
for i in range(m2):
    mat2[i]=list(map(int,input().split()))
m3,n3=map(int,input().split())
mat3=[[0]*n3 for _ in range(m3)]
for i in range(m3):
    mat3[i]=list(map(int,input().split()))
if n1 != m2 or m1 != m3 or n2 != n3:
    print("Error!")
else:
    mat4=[[0]*n2 for _ in range(m1)]
    for i in range(m1):
        for j in range(n2):
            for k in range(n1):
                mat4[i][j]+=mat1[i][k]*mat2[k][j]
            print(mat4[i][j]+mat3[i][j],end=' ')
        print()
