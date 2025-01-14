n,m=map(int,input().split())
l1=[]
ans=[]
l1.append([])
for _ in range(m+2):
    l1[0].append(0)
for i in range(n):
    l1.append([])
    l1[i+1].append(0)
    l1[i+1].extend(list(map(int,input().split())))
    l1[i+1].append(0)
l1.append([])
for _ in range(m+2):
    l1[n+1].append(0)
for i in range(1,n+1):
    ans.append([])
    for j in range(1,m+1):
        curr = l1[i-1][j-1]+l1[i-1][j]+l1[i-1][j+1]+l1[i][j-1]+l1[i][j+1]+l1[i+1][j-1]+l1[i+1][j]+l1[i+1][j+1]
        if curr == 3:
            ans[i-1].append(1)
        elif curr ==2 and l1[i][j] == 1:
            ans[i-1].append(1)
        else:
            ans[i-1].append(0)
for i in range(n):
    print(*ans[i])

# n, m = map(int, input().split())
# grid = [list(map(int, input().split())) for _ in range(n)]
# ans = [[0] * m for _ in range(n)]

# for i in range(n):
#     for j in range(m):
#         curr = sum(
#             grid[x][y] for x in (i-1, i, i+1) if 0 <= x < n
#             for y in (j-1, j, j+1) if 0 <= y < m
#         )
#         if curr == 3 or (curr == 2 and grid[i][j] == 1):
#             ans[i][j] = 1

# for row in ans:
#     print(*row)
