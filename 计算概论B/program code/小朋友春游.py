from collections import deque
n = int(input())
l1= list(map(int,input().split()))
l1.sort(reverse=True)
l2=[]
l3=[]
l4=[]
while len(l1)>0:
    if l1[-1] <=n:
        if l1[-1] in l2:
            l3.append(l1.pop())
        else:
            l2.append(l1.pop())
    else:
        l3.append(l1.pop())
for i in range(1,n+1):
    if i not in l2:
        l4.append(i)
print(*l4)
print(*l3)