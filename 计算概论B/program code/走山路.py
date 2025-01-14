import heapq
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n, m, p = map(int, input().split())
matrix = [list((input().split())) for _ in range(n)]
se = [list(map(int, input().split())) for _ in range(p)]

neighbor = [[] for _ in range(n*m)]
for i in range(n):
    for j in range(m):
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if 0 <= ni < n and 0 <= nj < m:
                if matrix[i][j].isdigit() and matrix[ni][nj].isdigit():
                    neighbor[i*m+j].append((ni*m+nj,
                                           abs(int(matrix[i][j]) - int(matrix[ni][nj]))))
se_ = []
for i in reversed(range(len(se))):
    s = se[i][0]*m + se[i][1]
    e = se[i][2]*m + se[i][3]
    se_.append((s, e))
while se_:
    s, e = se_.pop()
    distance = [float("inf")] * (n*m)
    distance[s] = 0
    vis = set()
    q = [(0, s)]
    while q:
        _,u=heapq.heappop(q)
        if u in vis:
            continue
        vis.add(u)
        for v,w in neighbor[u]:
            # print(distance)
            # print(v,u)
            if distance[v] > distance[u] + w:
                distance[v] = distance[u]+w
                heapq.heappush(q,(distance[v],v))
    print(distance[e] if distance[e] != float("inf") else "NO")
