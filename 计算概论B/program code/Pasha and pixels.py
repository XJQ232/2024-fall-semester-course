rows,columns,moves = map(int,input().split())
check = []
for i in range(rows):
    check.append([])
    for j in range(columns):
        check[i].append(True)
if rows < 2 or columns < 2:
    print("0")
    exit()
for i in range(moves):
    a,b=map(int,input().split())
    check[a-1][b-1]=False
    if 2<=  a <= rows-1:
        if 2<= b <= columns-1:
            if not(check[a-2][b-1] or check[a-2][b-2] or check[a-1][b-2]) or not (check[a-2][b] or check[a-2][b-1] or check[a-1][b]) or not (check[a][b-1] or check[a-1][b-2] or check[a][b-2]) or not (check[a-1][b] or check[a][b] or check[a][b-1]):
                print(i+1)
                exit()
        elif b == columns:
            if not(check[a-2][b-1] or check[a-2][b-2] or check[a-1][b-2])  or not (check[a][b-1] or check[a-1][b-2] or check[a][b-2]) :
                print(i+1)
                exit()
        elif b == 1:
            if not (check[a-2][b] or check[a-2][b-1] or check[a-1][b]) or not (check[a-1][b] or check[a][b] or check[a][b-1]):
                print(i+1)
                exit()
    elif a == rows:
        if 2<= b <= columns-1:
            if not(check[a-2][b-1] or check[a-2][b-2] or check[a-1][b-2]) or not (check[a-2][b] or check[a-2][b-1] or check[a-1][b]):
                print(i+1)
                exit()
        elif b == columns:
            if not(check[a-2][b-1] or check[a-2][b-2] or check[a-1][b-2]):
                print(i+1)
                exit()
        elif b == 1:
            if not (check[a-2][b] or check[a-2][b-1] or check[a-1][b]):
                print(i+1)
                exit()
    elif a == 1:
        if 2<= b <= columns-1:
            if not (check[a][b-1] or check[a-1][b-2] or check[a][b-2]) or not (check[a-1][b] or check[a][b] or check[a][b-1]):
                print(i+1)
                exit()
        elif b == columns:
            if not (check[a][b-1] or check[a-1][b-2] or check[a][b-2]) :
                print(i+1)
                exit()
        elif b == 1:
            if not (check[a-1][b] or check[a][b] or check[a][b-1]):
                print(i+1)
                exit()           
print("0")