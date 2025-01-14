n = int(input())
l1=list(map(int,input().split()))
check = [True]*n
curr = 1
l2=[]
l1.sort()
# for i in range(n):
#     curr = l1[i]
#     if not check[i]:
#         continue
#     else:
#         check[i] = False
#         ans += 1
#         for j in range(i,n):
#             if check[j] and curr < l1[j]:
#                 curr = l1[j]
#                 check[j] = False
if n==1:
    print("1")
    exit()
for i in range(n-1):
    if l1[i]==l1[i+1]:
        curr += 1
    else:
        l2.append(curr)
        curr = 1
    if i == n-2:
        l2.append(curr)
n = len(l2)
for i in range(n-1):
    if l2[i] > l2[i+1]:
        l2[i+1] = l2[i]
ans = l2[n-1]
print(ans)
