n = int(input())
l1 = sorted(map(int,input().split()))
m = int(input())
def find(l1,coins,left,right):
    if left == right:
        if coins >= l1[left]:
            print (left + 1)
        else:
            print (left)
        return
    mid = (left + right)//2
    if coins >= l1[mid] and (mid == n-1 or coins < l1[mid + 1]):
        print (mid + 1)
        return
    if coins < l1[mid]:
        find (l1,coins,left,mid)
    else:
        find(l1,coins,mid+1,right)
        

for _ in range(m):
    coins = int(input())
    find(l1,coins,0,n-1)