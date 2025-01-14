import sys
sys.setrecursionlimit(1000000)
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    l1=[ ]
    l2=[]
    for j in range(1,len(arr)):
        if arr[j] >= arr[0]:
            l1.append(arr[j])
        else:
            l2.append(arr[j])
    return quicksort(l2)+[arr[0]]+quicksort(l1)

l1=list(map(int,input().split()))
print(*quicksort(l1))