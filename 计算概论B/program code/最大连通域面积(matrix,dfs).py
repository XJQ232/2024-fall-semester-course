Test = int(input())
dx = [0,0 ,1 ,1,1,-1,-1,-1]
dy = [1,-1,-1,0,1,-1, 0, 1]

def check(mat,x,y):
    if x in range(n) and y in range(m) and mat[x][y] == 'W':
        return True
    return False

for _ in range(Test):
    n,m = map(int,input().split())
    matrix = [[] for _ in range(n)]
    max1 = 0
    stack = [(0,0)]
    
    for i in range(n):
        matrix[i] = list(input())
        for j in range(m):
            if matrix[i][j] == 'W':
                stack.pop()
                stack.append((i,j))
    # print(stack)
    while True:
        # print(stack,)
        curr = 0
        while stack:
            x,y = stack.pop()
            if matrix[x][y] == 'W':
                curr += 1
                matrix[x][y] = '.'
                for i in range(8):
                    nx,ny = x+dx[i],y+dy[i]
                    if check(matrix,nx,ny):
                        stack.append((nx,ny))
        max1 = max(max1,curr)
        # print(matrix,max)
        stat = False
        for i in range(n):
            if stat:break
            for j in range(m):
                if matrix[i][j] == 'W':
                    stack.append((i,j))
                    stat = True
                    break
        if not stack:break
    print(max1)