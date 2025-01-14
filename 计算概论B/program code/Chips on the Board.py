n = int(input())
for i in range(n):
    m = int(input())
    row = list(map(int,input().split()))
    line = list(map(int,input().split()))
    row.sort();line.sort()
    min1=row[0]*m+sum(line)
    min2=line[0]*m+sum(row)
    print(min(min1,min2))