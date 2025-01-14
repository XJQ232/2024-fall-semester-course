N = int(input())
for _ in range(N):
    E,F = map(int,input().split())
    W = F - E
    dp = [0]+[float('inf')]*W
    n = int(input())
    price =[]
    weight =[]
    for i in range(n):
        p,w = map(int,input().split())
        price.append(p)
        weight.append(w)
    for i in range(n):
        for j in range(W+1-weight[i]):
            dp[j+weight[i]] = min(dp[j+weight[i]],dp[j]+price[i])
    if dp[-1] != float('inf'):
        print(f"The minimum amount of money in the piggy-bank is {dp[-1]}.")
    else:
        print('This is impossible.')