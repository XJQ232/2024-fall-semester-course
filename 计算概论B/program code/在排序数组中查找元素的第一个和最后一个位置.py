nums = list(map(int,input().split()))
target = int(input())
len1 = len(nums)
left = 0
right = len1
x,y = -1,-1
while left < right:
    mid = (left+right)//2
    if nums[mid] == target:
        x = mid
        right = mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid
    print(left,right)
print("1")
left = 0
right = len1
while left < right:
    mid = (left+right)//2
    if nums[mid] == target:
        y = mid
        left = mid + 1
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid
    print(left,right)
ans = '['+str(x)+','+str(y)+']'
print(ans)