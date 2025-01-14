n,m = map(int,input().split())
matrix1=[list(map(int,input().split())) for _ in range(n)]
visited = [[False]* m for _ in range(n)]
stack = [(0,0,-1,0)]
dx = [1,0,0,-1]
dy = [0,-1,1,0]
visited[0][0]=True
while stack:
    
    x,y,dire,temp = stack.pop()
    sum1 = 0
    count = 0
    next1 = matrix1[x][y]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<= nx < n and 0<= ny < m:
            if dire != i:
                sum1 += matrix1[nx][ny]
                count += 1
            else:
                sum1 += temp
                count += 1
            if not visited[nx][ny]:
                stack.append((nx,ny,4-i,next1))
                visited[nx][ny] =True
    print(x,y,count,sum1)
    matrix1[x][y] = sum1//(count+1)
print(matrix1)