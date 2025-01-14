n = int(input())
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
l3 = [l1[l2[i]-1]*(n-i-1) for i in range(n)]
# print(l3,sum(l3))
sum1 = sum(l3)/n
print("%.2f" % sum1)