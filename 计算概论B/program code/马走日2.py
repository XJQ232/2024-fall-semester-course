n = int(input())
count = 0
dx= [1,1,2,2,-1,-1,-2,-2]
dy= [2,-2,1,-1,-2,2,1,-1]
def dfs(x,y,step):
    global count 
    if step == n*m:
        count += 1
        return
    for i in range(8):
        nx = x +dx[i]
        ny = y+dy[i]
        if 0<= nx < n and 0<= ny <m:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx,ny,step+1)
                visited[nx][ny] = False
    return
for _ in range(n):
    n,m,x,y = map(int,input().split())
    count = 0
    visited = [[False]*m for _ in range(n)]
    visited[x][y] = True
    dfs(x,y,1)
    print(count)