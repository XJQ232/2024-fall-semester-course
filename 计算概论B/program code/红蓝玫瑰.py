l1 = input()
len1 = len(l1)
dp1=[0]*(len1)
dp2=[1]+[0]*(len1-1)
dp1[1] = 1-(l1[0]==l1[1])
dp2[1] = 1-(l1[0]==l1[1])
for i in range(len1-1):
    if l1[i+1] == l1[i]:
        dp1[i+1] = min(dp1[i],1+dp2[i])
        dp2[i+1] = 1+dp1[i+1]
    else:
        dp1[i+1] = min(dp2[i],1+dp1[i])
        dp2[i+1] = 1+dp1[i]
if l1[-1] == 'B':
    print(min(dp1[-1]+1,dp2[-1]))
else:
    print(min(dp1[-1],dp2[-1]))