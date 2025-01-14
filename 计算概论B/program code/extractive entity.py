n = int(input())
total = 0
for i in range(n):
    str1 = list(map(str,input().split()))
    for j in range(len(str1)):
        if str1[j][0] == '#' and str1[j+1][0]!='#' and j<(len(str1))-1:
            total+=1
print (total)