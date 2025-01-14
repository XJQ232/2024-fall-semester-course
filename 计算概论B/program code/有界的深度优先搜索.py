n,m,l = map(int,input().split())
nei = [[] for _ in range(n)]
for _ in range(m):
    x,y = map(int,input().split())
    nei[x].append(y)
    nei[y].append(x)
s=int(input())
for _ in range(n):
    nei[_].sort()
ans=[s]
visited=set()
visited.add(s)
def dfs(x,step):
    
    if step == l:return
    for i in nei[x]:
        if i not in visited:
            ans.append(i)
            visited.add(i)
            dfs(i,step+1)
for i in nei[s]:
    if i not in visited:
        ans.append(i)
        visited.add(i)
        dfs(i,1)
print(*ans)