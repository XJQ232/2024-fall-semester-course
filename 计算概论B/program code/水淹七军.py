import sys
sys.setrecursionlimit(300000)
input = sys.stdin.read
data = input().split()
index1 = 1
K = int(data[0])
dx = [1,-1,0,0]
dy = [0,0,1,-1]
result = []
def check(mat,x,y,m,n,h):
    if 0<=x and x < m and 0<= y and y < n and mat[x][y] < h: return True
    return False
for _ in range(K):
    M ,N = map(int,data[index1:index1+2])
    index1 += 2
    matrix = [[] for _ in range(M)]
    flooded = [[False]*N for _ in range(M)]
    cases=[]
    for i in range(M):
        matrix[i]=list(map(int,data[index1:index1+N]))
        index1+=N
    idx,idy = map(int,data[index1:index1+2])
    index1+=2
    p = int(data[index1])
    index1+=1
    stat = False
    for i in range(p):
        x,y = map(int,data[index1:index1+2])
        index1+=2
        cases.append((x,y))
    inq = set()
    for a,b in cases:
        if stat:break
        stack=[(a-1,b-1)]
        # print(stack)
        # print(flooded)
        height = matrix[a-1][b-1]
        while stack:
            x,y= stack.pop()
            inq.add((x,y))
            if x == idx -1 and y == idy -1:
                stat = True
                break
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if check(matrix,nx,ny,M,N,height) and (nx,ny) not in inq:
                    stack.append((nx,ny))
    
    result.append("Yes" if stat else "No")
sys.stdout.write("\n".join(result)+"\n")