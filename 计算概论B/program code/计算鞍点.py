matrix= [list(map(int,input().split())) for _ in range(5)]
x1=[0,0,0,0,0]
y1=[0,0,0,0,0]
count = 0
ans=[]
for k in range(5):
    maxi = 0
    minj = float("inf")
    for l in range(5):
        if maxi < matrix[k][l]:
            maxi = matrix[k][l]
            x1[k]=l
        if minj > matrix[l][k]:
            minj = matrix[l][k]
            y1[k] = l
for i in range(5):
    if y1[x1[i]]==i:
        count += 1
        ans.append((i+1,x1[i]+1,matrix[i][x1[i]]))
if count:
    for x,y,z in ans:
        print(x,y,z)
else:
    print("not found")