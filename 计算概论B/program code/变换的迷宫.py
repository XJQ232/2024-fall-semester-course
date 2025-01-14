from collections import deque
testnumber = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def check(x, y, t):
    if 0 <= x < R and 0 <= y < C:
        if (t+1) % K == 0:
            return True
        else:
            if matrix[x][y] == '.':
                return True
    return False


for _ in range(testnumber):
    R, C, K = map(int, input().split())
    matrix = [list(input()) for _ in range(R)]
    need_checkstart = True
    need_checkend = True
    for i in range(R):
        if need_checkstart or need_checkend:
            for j in range(C):
                if matrix[i][j] == 'S':
                    sx, sy = i, j
                    matrix[i][j] = '.'
                    need_checkstart = False
                if matrix[i][j] == 'E':
                    ex, ey = i, j
                    matrix[i][j] = '.'
                    need_checkend = False
    stack = deque()
    stack.append((sx, sy, 0))
    inq = set((sx, sy, 0))
    while stack:
        x, y, time = stack.popleft()
        if x == ex and y == ey:
            print(time)
            break
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if check(nx, ny, time):
                if (nx, ny, (1+time) % K) not in inq:
                    stack.append((nx, ny, time+1))
                    inq.add((nx, ny, (1+time) % K))
    else:
        print("Oop!")
