num,total=map(int,input().split())
value=[0]*num
weight=[0]*num
output=[0]*(total+1)
for _ in range(num):
    a,b=map(int,input().split())
    value[_]=a
    weight[_]=b
for i in range(num):
    for j in range(total,weight[i]-1,-1):
        if output[j] < output[j - weight[i]] + value[i]:
            output[j]=output[j - weight[i]] + value[i]
ans = format(max(output),".1f")
print(ans)