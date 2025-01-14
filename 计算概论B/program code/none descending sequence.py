n = int(input())
l1 = list(map(int,input().split()))
l2 = sorted(l1)
if l2 == l1:
    print("YES")
else:
    print("NO")