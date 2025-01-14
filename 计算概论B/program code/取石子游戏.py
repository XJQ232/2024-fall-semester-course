n,m = map(int,input().split())
def dfs(a,b):
    if a%b == 0:
        return True
    if a // b == 1:
        return not dfs(b,a%b)
    return True
while n:
    n,m = max(n,m),min(n,m)
    ans = dfs(n,m)
    print("win" if ans else "lose")
    n,m = map(int,input().split())