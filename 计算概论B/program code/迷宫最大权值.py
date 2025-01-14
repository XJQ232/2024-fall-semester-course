n, m = map(int, input().split())
matrix = [[] for _ in range(n)]
value = [[] for _ in range(n)]
visited = [[False]*m for _ in range(n)]
for i in range(n):
    matrix[i] = list(map(int, input().split()))
for i in range(n):
    value[i] = list(map(int, input().split()))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited[0][0] = True
stat = False
max1 = 0


def check(x, y):
    if x in range(n) and y in range(m) and not matrix[x][y] and not visited[x][y]:
        return True
    return False


def dfs(x, y, curr):
    global stat
    global max1
    # print(x,y,curr)
    if x == n-1 and y == m - 1:
        stat = True
        max1 = max(curr, max1)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if check(nx, ny):
            visited[nx][ny] = True
            dfs(nx, ny, curr+value[nx][ny])
            visited[nx][ny] = False


dfs(0, 0, value[0][0])
# print(matrix)
# print(value)
if stat:
    print(max1)
else:
    print("-1")
