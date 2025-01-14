n1,m1,n2,m2 = map(int,input().split())
matrix1 =[]
matrix2 =[]
for _ in range(n1):
    l1 = list(map(int,input().split()))
    matrix1.append(l1)
for _ in range(n2):
    l1 = list(map(int,input().split()))
    matrix2.append(l1)
for i in range(n1-n2+1):
    for j in range(m1-m2+1):
        curr = 0
        for k1 in range(n2):
            for k2 in range(m2):
                curr += matrix2[k1][k2]*matrix1[k1+i][k2+j]
        print(curr,end=' ')
    print()