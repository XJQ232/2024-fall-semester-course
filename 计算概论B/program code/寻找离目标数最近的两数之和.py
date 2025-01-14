from bisect import bisect_right
n = int(input())
l1 = sorted(list(map(int, input().split())))
len1 = len(l1)
id1 = 0
id2 = len1-1
min1 = l1[id1] + l1[id2]
while id1 < id2:
    curr =l1[id1]+l1[id2]
    if abs(min1 - n) == abs(curr-n):min1 = min(min1,curr)
    if abs(min1 - n) > abs(curr-n):min1 = curr
    if curr < n:
        id1 += 1
    if curr > n:
        id2 -= 1
    if curr == n:
        min1 = n
        break
print(min1)