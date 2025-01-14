n = int(input())
matrix=[[1]*(n+2) for _ in range(n+2)]
check=[[True]*(n+2) for _ in range(n+2)]
dirc = [(-1,0),(1,0),(0,-1),(0,1)]
l1={'x':(0,1),'y':(1,0)}
start=[]
for i in range(1,n+1):
    matrix[i][1:n] = list(map(int,input().split()))
    for j in range(1,n+1):
        if matrix[i][j] == 9:
            endx=i
            endy=j
        if matrix[i][j] == 5:
            start.append((i,j))
# print(start,endx,endy)
# print(matrix)
if start[0][0]==start[1][0]:
    stat = 'x'
else:
    stat = 'y'
pos=[start[0]]
while pos:
    x,y=pos.pop()
    # print(pos)
    # print(x,y)
    # print(matrix)
    # print(check)
    
    if x==endx and y == endy:
        print("yes")
        break
    if x+l1[stat][0] == endx and y+l1[stat][1] == endy:
        print("yes")
        break
    check[x][y] = False
    for i,j in dirc:
        if check[x+i][y+j]:
            if matrix[x+i][y+j] != 1 and matrix[x+i+l1[stat][0]][y+j+l1[stat][1]] != 1:
                pos.append((x+i,y+j))
else:
    print("no")