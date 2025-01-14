from collections import deque
n,m,k = map(int,input().split())
matrix = [[] for _ in range(n)]
for i in range(n):
    matrix[i]=list(map(int,input().split()))
inqueue=set((0,0))
dx = [1,-1,0,0]
dy = [0,0,1,-1]
stack = deque([(0,0)])
step = 0
while step <= k:
    curr = stack.copy()
    while curr:
        x,y = curr.pop()
        stack.popleft()
        if x== n-1 and y == m-1 and step == k:
            print("Yes")
            exit()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if nx in range(n) and ny in range(m) and matrix[nx][ny] == 0:
                matrix[nx][ny] = 1
                stack.append((nx,ny))
    step+= 1
else:print("No")