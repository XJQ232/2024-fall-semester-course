dx = [0,0,1,-1]
dy = [1,-1,0,0]
n = int(input())
from collections import deque
matrix = []
for i in range(n):
    matrix.append(list(input()))
stack1 = deque()

def dfs(x,y):
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if matrix[nx][ny] == '1':
                matrix[nx][ny] = '2'
                stack1.append((nx,ny,0))
                dfs(nx,ny)
    return

def solve():
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == '1':
                matrix[i][j] = '2'
                stack1.append((i,j,0))
                dfs(i,j)
                return

solve()

while stack1:
    x,y,step = stack1.popleft()
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<= nx and nx < n and 0<= ny and ny < n:
            if matrix[nx][ny] == '1':
                print(step)
                exit()
            if matrix[nx][ny] == '0':
                stack1.append((nx,ny,step+1))
                matrix[nx][ny] = '2'