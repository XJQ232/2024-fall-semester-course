n,m = map(int,input().split())
check = [[True]*(m+2) for _ in range(n+2)]
matrix = [[0]*(m+2) for _ in range(n+2)]

for _ in range(1,n+1):
    matrix[_][1:-2] = list(map(int,input().split()))
dirct = [(-1,0),(1,0),(0,-1),(0,1)]
stat = False
for i in range(1,n+1):
    if stat:
        break
    for j in range(1,m+1):
        if matrix[i][j] == 1 and check[i][j]:
            stack = {(i,j)}
            stat = True
            break
else:
    print("0")
    exit()
count = 0
while stack:
    count += 4
    x,y = stack.pop()
    check[x][y]= False
    for dx,dy in dirct:
        if matrix[x+dx][y+dy]:
            if not check[x+dx][y+dy]:
                count -= 2
            else:
                stack.add((x+dx,y+dy))
print(count)