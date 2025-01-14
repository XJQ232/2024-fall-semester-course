n = int(input())
v1= list(map(int,input().split()))
s1=[v1[0]]
for i in range(1,n):
    s1.append(s1[i-1]+v1[i])
v1.sort()
s2=[v1[0]]
for i in range(1,n):
    s2.append(s2[i-1]+v1[i])
m = int(input())
for _ in range(m):
    type,l,r = map(int ,input().split())
    if type == 1:
        if l>1:
            print(s1[r-1]-s1[l-2])
        else:
            print(s1[r-1])
    else:
        if l > 1:
            print(s2[r-1]-s2[l-2])
        else:
            print(s2[r-1])