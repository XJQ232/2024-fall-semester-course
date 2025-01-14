from collections import deque

n,m = map(int,input().split())
matrix = [[] for i in  range(n)]
visited = set()
dx=[0,0,1,-1]
dy=[-1,1,0,0]
def check(mat,x,y):
    if x in range(n) and y in range(m) and mat[x][y] != 2 and (x,y) not in visited:return True
    else:return False
for _ in range(n):
    matrix[_] = list(map(int,input().split()))
stack = deque([(0,0)])
step = -1
stat = True
while stack and stat:
    step += 1
    curr = stack.copy()
    # print(step)
    # print(curr)
    # print()
    while curr and stat:
        
        x,y = curr.pop()
        stack.popleft()
        visited.add((x,y))
        # print(x,y)
        # print(stack)
        # print(curr)
        if matrix[x][y] == 1:
            print(step)
            stat = False
            break
        for i in range(4):
            if check(matrix,x+dx[i],y+dy[i]):
                stack.append((x+dx[i],y+dy[i]))
        # print(x,y)
        # print(stack)
        # print(curr)
        # print()
if stat:print("NO")
    