n = int(input())
a,b = map(int,input().split())
l1 = []
for _ in range(n):
    x,y = map(int,input().split())
    l1.append((x*y,x,y))
l1.sort()
# print(l1)
sum1 = a
for i in range(n-1):
    sum1 *= l1[i][1]
sum1 = sum1//(l1[-1][-1])
print(sum1)