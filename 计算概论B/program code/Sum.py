n = int(input())
l1=[]*3
for i in range(n):
    l1=list(map(int,input().split()))
    l1.sort()
    if l1[2] == l1[0]+l1[1]:
        print("YES")
    else:
        print("NO")