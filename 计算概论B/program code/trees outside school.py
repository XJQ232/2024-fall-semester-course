L,M=map(int,input().split())
b=[1]*(L+1)
for i in range(M):
    m,n=map(int,input().split())
    for i in range(m,n+1):
        b[i]=0
sum=0
for i in range(L+1):
    sum+=b[i]
print(sum)