n,p=map(int,input().split())
check=[]
for i in range(n):
    line = []
    for j in range(n):
        line.append(False)
    check.append(line)
for _ in range(p):
    x,y=map(int,input().split())
    check[x-1][y-1]=True
    if check[y-1][x-1]:print("Yes");exit()
print("No")