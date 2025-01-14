n = int(input())
import  sys
sys.setrecursionlimit(1<<30)
import  heapq
for _ in range(n):
    l,r,x = map(int,input().split())
    a,b = map(int,input().split())
    r= r-l
    a= a-l
    b= b-l
    l=0
    t= r-l
    matrix=[[] for _ in range(t+1)]
    for i in range(t+1):
        for j in range(i,t+1):
            if abs(i-j)>=x:
                matrix[i].append((j,1))
                matrix[j].append((i,1))
    dis=[float("inf")]*(t+1)
    dis[a]=0
    stack=[(0,a)]
    vis=set()
    while stack:
        _,u = heapq.heappop(stack)
        if u in vis:
            continue
        vis.add(u)
        for v,w in matrix[u]:
            if dis[v]>dis[u]+w:
                dis[v]=dis[u]+w
                heapq.heappush(stack,(dis[v],v))
    print(dis[b] if dis[b] != float("inf") else "-1")