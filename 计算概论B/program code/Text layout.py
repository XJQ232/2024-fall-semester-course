n = int(input())
l1=list(input().split())
curr = 0
for i in range(n):
    curr+=len(l1[i])
    if curr<=80:
        print(l1[i],end='')
        if i<n-1 and curr + len(l1[i+1])+1<=80:
            print(' ',end='')
            curr+=1
        else:
            print()
            curr = 0