a = list(map(int,input().split()))
b=set()
c=[]
for i in range(a[0]):
    c=list(map(int,input().split()))
    b.update(c[1:])
if len(b) == a[1]:
    print("YES")
else:
    print("NO")

# n,m=[int(x) for x in input().split()]
# a=[]
# flag=0
# for _ in range(n):
#     b=[int(x) for x in input().split()]
#     for i in range(1,len(b)):
#         a.append(b[i])
# if len(set(a)) < m:
#     print("no")
# else:
#     print("yes")