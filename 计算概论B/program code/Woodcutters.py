n = int(input())
lx = []
lh = []
for _ in range(n):
    x,h = map(int,input().split())
    lx.append(x)
    lh.append(h)
if n == 1:
    print(1)
else:
    curr = lx[0]
    total = 1
    for i in range(1,n-1):
        if lx[i] - lh[i] > curr:
            curr = lx[i]
            total += 1
            continue
        if lx[i] + lh[i] < lx[i+1]:
            curr = lx[i] + lh[i]
            total += 1
            continue
        else:
            curr = lx[i]
    total += 1
    print(total)
