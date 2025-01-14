n = int(input())
def work(m,max1):
    global a
    if m <= max1:
        return a[m]
    for i in range(max1,m+1):
        a[i] = 2*a[i-1]+a[i-2]
        a[i] %= 32767
    return a[m]
a=[0]*1000001
a[1]=1
a[2]=2
max1 = 2
for i in range(n):
    curr = int(input())
    print(work(curr,max1))
    max1 = max(max1,curr)