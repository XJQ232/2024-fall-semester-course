n = int(input())
matrix = [[] for _ in range(n)]
ans = []
direction = [(0,1),(1,0),(0,-1),(-1,0)]
check = [[True] * n for _ in range(n)]
for i in range(n):
    matrix[i] = list(map(int,input().split()))
stack = [(0,0)]
dirc = 0
count = 1
while stack and count <= 4:
    x,y = stack.pop()
    ans.append(matrix[x][y])
    check[x][y] = False
    dx,dy = direction[dirc]
    if x+dx in range(n) and y+dy in range(n) and check[x+dx][y+dy]:
        stack.append((x+dx,y+dy))
        count = 1
    else:
        count += 1
        ans.pop()
        stack.append((x,y))
        dirc = (dirc+1)%4
ans.append(matrix[x][y])
print(ans)