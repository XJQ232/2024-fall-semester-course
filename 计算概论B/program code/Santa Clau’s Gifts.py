num,total=map(int,input().split())
value=[0]*num
weight=[0]*num
output=[0]*(total+1)
for _ in range(num):
    a,b=map(int,input().split())
    value.append(a)
    weight.append(b)
output[weight[0]]=value[0]
for i in range(num):
    if output[weight[i]]<value[i]:
        output[weight[i]]=value[i]
    for j in range(weight[i]):
        if j + weight[i]< total and output[j + weight[i]] < output[j] + value[i]:
            output[j + weight[i]]=output[j] + value[i]
ans = format(max(output),".1f")
print(ans)