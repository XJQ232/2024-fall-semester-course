from itertools import product
from copy import deepcopy
l1 = list(product([0,1],repeat=6))
matrix=[list(map(int,input().split())) for _ in range(5)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for l2 in l1:
    temp1=deepcopy(matrix)
    l3=[list(l2)]
    for i in range(6):
        if l3[0][i]:
            temp1[0][i]=1^temp1[0][i]
            for k in range(4):
                nx = 0 + dx[k]
                ny = i + dy[k]
                if 0<=nx<5 and 0<= ny < 6:
                    temp1[nx][ny] = 1^temp1[nx][ny]
    for i in range(1,5):
        l3.append([])
        for j in range(6):
            # print(l3)
            if temp1[i-1][j]:
                l3[i].append(1)
                temp1[i][j]=1^temp1[i][j]
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0<=nx<5 and 0<= ny < 6:
                        temp1[nx][ny] = 1^temp1[nx][ny]
            else:
                l3[i].append(0)
    if sum(temp1[-1]) == 0:
        for i in range(5):
            print(*l3[i])
        exit()