n = int(input())
l1 = list(input().split())
len1 = len(l1)
l2=[]
for i in range(10):
    l2.append([])
for i in l1:
    l2[int(i[0])].append(i)
for i in range(1,10):
    len2 = len(l2[i])
    for j in range(len2-1):
        for k in range(j+1,len2):
            num1 = int(l2[i][j]+l2[i][k])
            num2 = int(l2[i][k]+l2[i][j])
            if num1 <= num2:
                c = l2[i][j]
                l2[i][j] = l2[i][k]
                l2[i][k] = c
max1=''
min1=''
for i in range(9,0,-1):
    for j in l2[i]:
        max1 = max1+j
    l2[i].reverse()
for i in range(1,10):
    for j in l2[i]:
        min1 = min1 + j
print(max1,min1)