n = int(input())
l1 = [1,2,4,8,16,32,64,128,256,512,1024]
for _ in range(n):
    m = int(input())
    l0=list(map(int,input().split()))
    l2={}
    curr = 0
    for x in l1:
        curr = (curr+l0.count(x))//2
        l2[x] = (curr+l0.count(x))%2
    l2[2048]=curr+l0.count(2048)
    if l2[2048]:
        print("YES")
    else:
        print("NO")

