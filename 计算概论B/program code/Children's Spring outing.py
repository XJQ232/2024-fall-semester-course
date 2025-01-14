n = int(input())
l1= list(map(int,input().split()))
b=[0]*(n+1)
l1.sort()
for i in range(1,n+1):  
    if not i in l1:
        print(i,end=' ')
    else:
        b[i]+=1
print()
for i in l1:
    if not i in range(n+1):
        print (i,end=' ')
