n,m = map(int,input().split())
l1=sorted(list(map(int,input().split())))
l2=[]
for i in range(n-1):
    l2.append(l1[i+1]-l1[i])
total = 0
l2.sort()
for i in range(n-m):
    total += l2[i]
print(total)