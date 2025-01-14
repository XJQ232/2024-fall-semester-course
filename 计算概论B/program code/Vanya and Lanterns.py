n,l = map(int,input().split())
max1 = 0
d=list(map(int,input().split()))
d.sort()
max1 = max(d[0],l-d[n-1])
for i in range(n-1):
    max1 = max(max1,(d[i+1]-d[i])/2)
print(max1)
