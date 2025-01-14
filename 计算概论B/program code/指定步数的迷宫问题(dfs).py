n,m,k = map(int,input().split())
stat = False
matrix = [[] for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def check(mat,x,y):
    if x in range(n) and y in range(m) and mat[x][y] == 0:return True
    return False

def dfs(mat,x,y,step):
    global stat
    if stat:return
    if x==n-1 and y == m-1 and step == k:
        stat = True
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        # print(nx,ny,step)
        if check(mat,nx,ny):
            mat[nx][ny] = 1
            dfs(mat,nx,ny,step+1)
            mat[nx][ny] = 0


for i in range(n):
    matrix[i]=list(map(int,input().split()))
stack = [(0,0)]
dfs(matrix,0,0,0)
print("Yes" if stat else "No")
