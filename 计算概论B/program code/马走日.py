from collections import deque
import sys
sys.setrecursionlimit(1<<30)
count = 0
def check(mat,x,y):
    if x in range(n) and y in range(m) and mat[x][y] == 0:
        return True
    return False

def dfs(mat, x, y):
    global count
    if len(inqueue) == total:
        count += 1
        return
    for i in range(8):
        nx, ny = x+dx[i], y+dy[i]
        # print(nx,ny,count)
        if check(mat,nx,ny):
            mat[nx][ny] = 1
            inqueue.add((nx,ny))
            dfs(mat, nx, ny)
            mat[nx][ny] = 0
            inqueue.remove((nx,ny))

Test = int(input())

for _ in range(Test):
    count = 0
    n, m, x, y = map(int, input().split())
    dx = [1, 1, -1, -1, 2, -2, 2, -2]
    dy = [2, -2, 2, -2, 1, 1, -1, -1]
    matrix = [[0]*m for _ in range(n)]
    matrix[x][y] = 1
    total = n*m
    inqueue = set()
    inqueue.add((x,y))
    dfs(matrix, x, y)
    print(count)
