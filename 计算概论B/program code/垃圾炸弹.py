d = int(input())
n = int(input())
map1 = []
max1 = 0
l1 = [0]*(1025)
for _ in range(1025):
    map1.append(l1.copy())
for _ in range(n):
    x, y, z = map(int, input().split())
    for i in range(max(x-d,0),min(x+d+1,1025)):
        for j in range(max(y-d,0),min(y+d+1,1025)):
            map1[i][j] += z
            if map1[i][j] > max1:
                max1 = map1[i][j]
print(sum([map1[i].count(max1) for i in range(1025)]), max1)
