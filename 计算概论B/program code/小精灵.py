n,m,k = map(int,input().split())
dp=[[-1]*(m+1) for _ in range(k+1)]
dp[0][m]=n
def find():
    for i in range(k,-1,-1):
        for j in range(m,0,-1):
            if dp[i][j]!=-1:
                return i,j
for i in range(k):
    cost,damge=map(int,input().split())
    for p in range(m):
        for q in range(i+1,0,-1):
            if p+ damge<=m and dp[q-1][p+damge]!=-1:
                dp[q][p]=max(dp[q][p],dp[q-1][p+damge]-cost)
capture,life = find()
print(capture,life)