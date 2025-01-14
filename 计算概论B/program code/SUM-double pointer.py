n,k=map(int,input().split())
l1=list(map(int,input().split()))
total = 0
i=0
j=n-1
while i<j:
    if l1[i]+l1[j] == k:
        total+=1
    if l1[i]+l1[j] < k:
        i += 1
    else:
        j -= 1
print(total)
