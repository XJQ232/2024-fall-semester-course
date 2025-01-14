from collections import deque
M,N  = map(int,input().split())
test = 1
dx = [1,-1,0,0]
dy = [0,0,1,-1]
min1 = float("inf")

def check(x,y):
    if 0<=x and x<= M+1 and 0<= y and y <= N+1 and matrix[y][x] != 'X':return True
    return False
        
while M:
    matrix = [[0]*(M+2) for _ in range(N+2)]
    visited = [[False]*(M+2) for _ in range(N+2)]
    for i in range(N):
        matrix[1+i][1:M+1] = list(input())
    x1,y1,x2,y2 = map(int,input().split())
    ans=[]
    l = 0
    # print(matrix)
    while x1+x2+y1+y2:
        matrix[y2][x2] =' '
        stack = deque()
        stack.append((x1,y1,-1,0))
        inq = set()
        inq.add((x1,y1))
        stat = False
        while stack:
            if stat:break
            x,y,dirc,k = stack.popleft()
            # print(x,y,k)
            if y == y2 and x == x2:
                    # print(nx,ny,k + int(i!=dirc))
                    ans.append(k)
                    stat = True
                    break
            # print(x,y,k)
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                while check(nx,ny) and (nx,ny) not in inq:
                    stack.append((nx,ny,i,k+1))
                    inq.add((nx,ny))
                    nx += dx[i]
                    ny += dy[i]
        if not stat:ans.append(0)
        matrix[y2][x2] ='X'
        x1,y1,x2,y2 = map(int,input().split())
        l += 1
    print(f"Board #{test}:")
    for i in range(l):
        if ans[i]:
            print(f"Pair {i+1}: {ans[i]} segments.")
        else:
            print(f"Pair {i+1}: impossible.")
    print()
    test += 1
    M,N  = map(int,input().split())