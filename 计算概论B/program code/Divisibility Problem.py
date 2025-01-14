n = int(input())
a=['']*2
for i in range(n):
    a=list(map(int,input().split()))
    if a[0] % a[1] == 0:
        print('0')
    else:
        print(a[1]*(a[0]//a[1]+1) - a[0])