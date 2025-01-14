n,m = map(int,input().split())
l1=sorted(list(map(int,input().split())))
left = 0
right = l1[-1]-l1[0]+1
while left < right:
    mid = (left+right)//2
    currmin=l1[0]
    count = 1
    for i in range(1,n):
        if l1[i]-currmin > mid:
            currmin = l1[i]
            count += 1
    if count > m:
        left = mid + 1
    else:
        ans = mid
        right = mid
print(ans)
