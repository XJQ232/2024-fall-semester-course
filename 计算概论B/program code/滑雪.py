# dx = [1,-1,0,0]
# dy = [0,0,-1,1]
# n,m = map(int,input().split())
# matrix = [list(map(int,input().split())) for _ in range(n)]
# dp = [[0]*m for _ in range(n)]
# max1 = 0
# check = [[True] * m for _ in range(n)]
# def dfs(x,y):
#     if dp[x][y] > 0 :
#         return dp[x][y]
#     for i in range(4):
#         nx = x+dx[i]
#         ny = y+dy[i]
#         if 0<= nx < n and 0<= ny < m:
#             if matrix[x][y] > matrix[nx][ny]:
#                 dp[x][y] = max(dp[x][y],dfs(nx,ny))
#     dp[x][y] += 1
#     return dp[x][y]
# for i in range(n):
#     for j in range(m):
#         max1= max(max1,dfs(i,j))
# print(max1)
from functools import lru_cache

dx = [1,-1,0,0]
dy = [0,0,-1,1]
n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
max1 = 0
check = [[True] * m for _ in range(n)]
@lru_cache(maxsize=2048)
def work(x,y):
    
    temp1 = 0
    check1 = True
    for k in range(4):
        nx = x+dx[k]
        ny = y + dy[k]
        if 0<=  nx < n and 0<= ny < m:
            if matrix[x][y] > matrix[nx][ny]:
                if not check[nx][ny]:
                    temp1 = max(temp1,dp[nx][ny])
                else:
                    temp1 = max(work(nx,ny),temp1)
                check1 = False
    if check1:
        dp[x][y] = 1
        check[x][y] = False
        return 1
    return temp1+1

for i in range(n):
    for j in range(m):
        if check[i][j]:
            dp[i][j] = work(i,j)
            max1 = max(max1, dp[i][j])
print(max1)