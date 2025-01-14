list1=list(map(int,input().split()))
list1.sort()
sum=0
for i in list1:
    sum+=i
sum //= 3
print(sum-list1[0],sum-list1[1],sum-list1[2])