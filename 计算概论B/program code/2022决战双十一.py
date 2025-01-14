from collections import defaultdict
n, m = map(int, input().split())
price =[input().split() for _ in range(n)]
coupon = [input().split() for _ in range(m)]
temp = [0]*m
min1 = float("inf")

def dfs(id,sum1):
    global min1
    if id == n:
        cou = 0
        for i in range(m):
            curr = 0
            for s in coupon[i]:
                x,y = map(int,s.split('-'))
                if temp[i] >= x:
                    curr = max(curr,y)
            cou += curr
        min1 = min(min1,sum1 - sum1//300*50 - cou)
        return
    for s in price[id]:
        x,y = map(int,s.split(':'))
        temp[x-1] += y
        dfs(id+1,sum1+y)
        temp[x-1] -= y
dfs(0, 0)
print(min1)