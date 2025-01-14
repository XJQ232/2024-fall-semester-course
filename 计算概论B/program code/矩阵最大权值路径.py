n, m = map(int, input().split())
matrix = [[] for _ in range(n)]
visited = [[True]*m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans=[]

def check(mat, x, y):
    if x in range(n) and y in range(m) and mat[x][y]:
        return True
    return False


def dfs(mat, x, y, value,step):
    global max1
    global ans
    if x == n-1 and y == m-1:
        if value > max1:
            max1 = value
            ans = step.copy()
            # print(ans)
        return
    visited[x][y] = False
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if check(visited, nx, ny):
            step.append((nx,ny))
            dfs(mat, nx, ny, value+mat[nx][ny],step)
            step.pop()
    visited[x][y] = True


max1 = -float("inf")
for i in range(n):
    matrix[i] = list(map(int, input().split()))
visited[0][0] = False
dfs(matrix, 0, 0, matrix[0][0],[(0,0)])
for i in ans:
    x,y = i
    print(x+1,y+1)
