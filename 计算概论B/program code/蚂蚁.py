from bisect import bisect_right
n = int(input())
for _ in range(n):
    l,m = map(int,input().split())
    l1= sorted(list(map(int,input().split())))
    ans2 = max(l1[0],l-l1[0],l1[-1],l-l1[-1])
    id1=bisect_right(l1,l/2)
    ans1 = max(l1[id1-1],l-l1[id1])
    print(ans1,ans2)