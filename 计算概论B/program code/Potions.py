n = int(input())
l1 =list(map(int,input().split()))
import heapq
l2 = []
ans = n
life = 0
curr = 0
while curr < n:
    life += l1[curr]
    heapq.heappush(l2,l1[curr])
    if life < 0:
        a = heapq.heappop(l2)
        life -= a
        ans -= 1
    curr += 1
print(ans)