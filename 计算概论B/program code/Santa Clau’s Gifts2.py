num,total = map(int,input().split())
value=[0]*num
weight=[0]*num
average=[0]*num
average_1=[0]*num
for _ in range(num):
    a,b=map(int,input().split())
    value.append(a)
    weight.append(b)
    average.append(a/b)
curr_weight = 0
curr_index = 0
curr_value = 0
average_1.sort(range(num),key = lambda x:average[x],reverse=True)
while curr_weight <  total:
    if curr_index == num:
        break
    if curr_weight + weight[average_1[curr_index]] <= toatal:
        curr_weight += weight[average_1[curr_index]]
        curr_value += value[average_1[curr_index]]
    else:
        curr_value += average[average_1[curr_index]]*(total - curr_weight)
    curr_index+=1
print(curr_value,".1f")