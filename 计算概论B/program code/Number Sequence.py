from math import isqrt
import bisect
n = int(input())
max1 = 0
l1 = []
l2 = [0]
for _ in range(n):
    l1.append(int(input()))
    if l1[-1] > max1:
        max1 = l1[-1]
step = 1
curr = 0
total = 0
while total < max1:
    curr = curr + len(str(step))
    total = total + curr
    l2.append(total)
    step += 1
for i in range(n):
    id1 = bisect.bisect_left(l2,l1[i])
    case1 = l1[i] - l2[id1-1]
    step2 = 1
    while case1 > len(str(step2)):
        case1 -= len(str(step2))
        step2 += 1
    print(str(step2)[case1-1])