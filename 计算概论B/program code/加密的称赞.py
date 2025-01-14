n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
dire = 0
visited[0][0]=True
dx=[1,0,-1,0]
dy=[0,1,0,-1]
s = chr(matrix[0][0])
i = 1 
x=0
y=0
while i < n**2:
    nx = x + dx[dire]
    ny = y + dy[dire]
    if 0<= nx < n and 0<= ny < n and not visited[nx][ny]:
        visited[nx][ny]=True
        if matrix[nx][ny]:
            s = s+chr(matrix[nx][ny])
        else:break
        x = nx
        y =ny
        i+=1
    else:
        dire = (dire+1)%4
print(s)