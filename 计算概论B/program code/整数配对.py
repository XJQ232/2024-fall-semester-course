n,m = map(int,input().split())
l1= sorted(list(map(int,input().split())))
l2= sorted(list(map(int,input().split())))
i , j = 0, 0
while i < n and j < m:
    if l1[i] <= l2[j]:
        i += 1
        j += 1
    else:
        j += 1
print(i)