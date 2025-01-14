length,a,b,c = map(int,input().split())
l1=[a,b,c]
dp_max = [0]*(length+1)
for i in range(length+1):
    for j in l1:
        if i > j:
            if dp_max[i-j]:
                dp_max[i]=max(dp_max[i],dp_max[i-j]+1)
        if i==j:
            dp_max[i]=max(dp_max[i],1)
print(dp_max[length])