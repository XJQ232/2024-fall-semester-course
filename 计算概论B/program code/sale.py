n,m=map(int,input().split())
l1=list(map(int,input().split()))
l1.sort()
sum=0
for i in range(m):
    if l1[i]<0:
        sum+=l1[i]
print(-sum)