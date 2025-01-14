n,m = map(int,input().split())
l1 = list(map(int,input().split()))
count = 0
total = 0
while total <= m and count < n:
    total += l1[count]
    count += 1
print(count-1)