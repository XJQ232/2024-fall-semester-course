n = int(input())
b=True
for t in range(n):
    l1=list(map(int,input().split()))
    b=False
    for i in range(-1,2,2):
        for j in range(-1,2,2):
            for k in range(-1,2,2):
                for l in range(-1,2,2):
                    if i*l1[0]+j*l1[1]+k*l1[2]+l*l1[3] == 24 and not b:
                        print("YES")
                        b = True
    if not b:
        print("NO")