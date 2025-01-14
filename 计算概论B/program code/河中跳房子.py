l,n,m = map(int,input().split())
d=[0]
for _ in range(n):
    d.append(int(input()))
d.append(l)
d.sort()
left = 1
right=l
ans = 0
while left <= right:
    mid = (left+right)//2
    count = 0
    j = 0
    for i in range(1,n+2):
        if d[i]-d[j] < mid:
            count += 1
        else:
            j = i
    if count > m:
        right = mid - 1
    else:
        ans,left =mid, mid + 1
print(ans)