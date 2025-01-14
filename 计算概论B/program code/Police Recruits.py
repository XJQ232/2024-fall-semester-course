n = int(input())
curr = 0
total = 0
m=list(map(int,input().split()))
for i in range(n):
    if curr > 0:
        curr += m[i]
    else:
        if m[i]>0:
            curr = m[i]
        else:
            total +=1
print(total)