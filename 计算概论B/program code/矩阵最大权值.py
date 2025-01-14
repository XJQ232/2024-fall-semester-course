n, m = map(int, input().split())
matrix = [[] for _ in range(n)]
visited = [[True]*m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def check(mat, x, y):
    if x in range(n) and y in range(m) and mat[x][y]:
        return True
    return False


def dfs(mat, x, y, value):
    global max1
    if x == n-1 and y == m-1:
        max1 = max(max1, value)
        return
    visited[x][y] = False
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if check(visited, nx, ny):
            dfs(mat, nx, ny, value+mat[nx][ny])
    visited[x][y] = True


max1 = -float("inf")
for i in range(n):
    matrix[i] = list(map(int, input().split()))
visited[0][0] = False
dfs(matrix, 0, 0, matrix[0][0])
print(max1)
