from functools import cmp_to_key
from bisect import bisect_left

number_cases = int(input())
for _ in range(number_cases):
    n = int(input())
    temp = list(map(int,input().split()))
    l1 = [(temp[2*i],temp[2*i+1]) for i in range(n)]
    l1.sort()
    f1 = [l1[i][1] for i in range(n)]
    f1.reverse()
    dp = [float("inf")]*(n+1)
    for i in f1:
        dp[bisect_left(dp,i)] = i
    print(bisect_left(dp,float("inf")))
