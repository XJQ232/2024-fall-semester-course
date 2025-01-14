n,weight_max = map(int,input().split())
value = list(map(int,input().split()))
weight = list(map(int,input().split()))
dp_value = [0]*(weight_max+1)
max1 = 0
for i in range(n):
    if weight[i] <= weight_max:
        for j in reversed(range(weight_max+1-weight[i])):
            dp_value[weight[i]+j]=max(dp_value[weight[i]+j],dp_value[j]+value[i])
            max1 = max(max1,dp_value[weight[i]+j])
print(max1)