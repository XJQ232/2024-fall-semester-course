n = int(input())
l1 = list(map(int,input().split()))
dict1 = {}
l2=[]
for i in l1 :
    if i in dict1:
        dict1[i] += i
    else:
        dict1[i] = i
        l2.append(i)
l2.sort()
len1 = len(dict1)
dp1 = [0] * len1
dp2 = [0] * len1
dp1[0] = dict1[l2[0]]
max1 = dp1[0]
for i in range(1,len1):
    dp2[i] = max(dp1[i-1],dp2[i-1])
    if l2[i]-1 == l2[i-1]:
        if i>1:
            dp1[i] = max(dp1[i-2],dp2[i-1]) + dict1[l2[i]]
        if i == 1:
            dp1[i] =dict1[l2[i]]
    else:
        dp1[i] = max(dp2[i-1],dp1[i-1]) + dict1[l2[i]]
    max1 = max(max1,dp1[i],dp2[i])
print(max1)
