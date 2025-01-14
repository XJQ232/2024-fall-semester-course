n, m = map(int, input().split())
l1 = list(map(int, input().split()))
dp = [1]*n
dict1 = set()
for i in reversed(range(n)):
    dict1.add(l1[i])
    dp[i]= len(dict1)
for _ in range(m):
    id1 = int(input())-1
    print(dp[id1])
