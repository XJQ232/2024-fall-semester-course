
n,w = map(int,input().split())
l1=[]

right = 0
left = 0
for i in range(n):
    l1.append(int(input()))
    right += l1[-1]
    left = max(left,l1[-1])
right += 1
ans = 1
while left < right:
    mid = (left+ right)//2
    temp=0
    count = 1
    for i in range(n):
        if temp+l1[i] > mid:
            temp = l1[i]
            count += 1
        else:
            temp += l1[i]
    if count > w:
        left = mid + 1
    else:
        ans = mid
        right = mid
print(ans)